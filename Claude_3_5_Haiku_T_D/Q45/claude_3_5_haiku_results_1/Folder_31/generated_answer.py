from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if list(subset) == list(subset)[::-1]:
                    palindrome_set.add(''.join(subset))
    return palindrome_set