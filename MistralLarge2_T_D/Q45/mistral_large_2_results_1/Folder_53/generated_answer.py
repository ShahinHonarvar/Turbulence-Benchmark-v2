from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    english_letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes