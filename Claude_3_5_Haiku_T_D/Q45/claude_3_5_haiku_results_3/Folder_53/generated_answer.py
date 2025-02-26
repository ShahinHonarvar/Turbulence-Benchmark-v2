from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for length in range(6, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if list(subset) == list(subset)[::-1]:
                    palindrome = ''.join(subset)
                    palindrome_set.add(palindrome)
    return palindrome_set