from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:8] if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if len(candidate) >= 7 and list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set