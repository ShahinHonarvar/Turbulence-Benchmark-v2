from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(len(perm) - length + 1):
                candidate = perm[i:i + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes