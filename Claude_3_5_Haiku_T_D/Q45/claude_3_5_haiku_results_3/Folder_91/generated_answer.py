from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:7] if char.isalpha()]
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for length in range(3, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if len(candidate) >= 3 and list(candidate) == list(candidate)[::-1]:
                    palindrome = ''.join(candidate)
                    palindrome_set.add(palindrome)
    return palindrome_set