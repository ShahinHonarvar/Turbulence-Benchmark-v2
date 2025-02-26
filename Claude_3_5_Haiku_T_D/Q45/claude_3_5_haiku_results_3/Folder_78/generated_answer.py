from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) - 2):
            candidate = perm[i:i + 3]
            full_candidate = list(candidate)
            full_candidate.extend(list(reversed(candidate[:-1])))
            palindrome = ''.join(full_candidate)
            if len(set(full_candidate)) == len(full_candidate):
                palindrome_set.add(palindrome)
    return palindrome_set