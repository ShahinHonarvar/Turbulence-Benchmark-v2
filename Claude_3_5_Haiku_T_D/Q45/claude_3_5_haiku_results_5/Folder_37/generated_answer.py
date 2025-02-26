from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) * 2 + 1):
        for perm in set(permutations(letters, length)):
            for i in range(length // 2 + 1):
                if list(perm[:length // 2]) != list(perm[length // 2 + length % 2:])[::-1]:
                    break
            else:
                palindromes.add(''.join(perm))
    return palindromes