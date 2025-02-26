from itertools import permutations

def palindromes_between_indices(s):
    relevant_letters = [c.lower() for c in s[3:10] if c.isalpha()]
    if len(relevant_letters) < 7:
        return set()
    palindrome_set = set()
    for perm in set(permutations(relevant_letters, 7)):
        for mid_idx in range(7):
            candidate = list(perm)
            left_half = candidate[:mid_idx]
            right_half = candidate[mid_idx + 1:]
            mid_char = candidate[mid_idx]
            mirror_candidate = left_half + [mid_char] + list(reversed(right_half))
            palindrome = ''.join(mirror_candidate)
            if len(set(palindrome)) > 1:
                palindrome_set.add(palindrome)
    return palindrome_set