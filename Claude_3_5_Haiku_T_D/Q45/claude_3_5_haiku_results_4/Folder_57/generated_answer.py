from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:6] if char.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(letters) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if len(candidate) >= 5 and list(candidate) == list(candidate)[::-1]:
                    palindrome = ''.join(candidate)
                    palindromes.add(palindrome)
    return palindromes