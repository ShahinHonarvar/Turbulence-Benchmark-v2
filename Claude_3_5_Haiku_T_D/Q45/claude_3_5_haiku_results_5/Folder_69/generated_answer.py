from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for pivot_length in range(len(perm) + 1):
            left_half = perm[:pivot_length]
            right_half = perm[pivot_length:]
            palindrome_candidate = ''.join(left_half + tuple(reversed(right_half)))
            if len(palindrome_candidate) >= 4 and palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes