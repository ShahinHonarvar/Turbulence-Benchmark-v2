from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8]
    english_letters = [char for char in substring if char.isalpha()]
    english_letters = ''.join(english_letters).lower()
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes