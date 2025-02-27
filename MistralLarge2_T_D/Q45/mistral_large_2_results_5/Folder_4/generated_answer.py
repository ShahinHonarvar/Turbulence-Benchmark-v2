from itertools import permutations

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    substring = s[3:10].lower()
    valid_chars = [char for char in substring if char in english_letters]
    palindromes = set()
    for length in range(7, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes