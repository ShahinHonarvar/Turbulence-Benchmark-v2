from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for variant in [''.join(perm), ''.join(reversed(perm))]:
                if variant == variant[::-1]:
                    palindrome_set.add(variant)
    return palindrome_set