from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                candidate = perm[i:i + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set