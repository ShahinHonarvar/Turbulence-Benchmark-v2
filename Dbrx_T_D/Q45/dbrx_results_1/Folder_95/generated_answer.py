from collections import Counter

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palindromes = set()
    start, end = (7, 8)
    if start < 0 or end >= len(s) or start > end:
        return palindromes
    s_range = s[start:end + 1]
    english_letters_in_range = [c for c in s_range if c in english_letters]
    for i in range(len(english_letters_in_range)):
        for j in range(i, len(english_letters_in_range)):
            pal = ''.join(english_letters_in_range[i:j + 1])
            if len(pal) >= 3 and Counter(pal) == Counter(pal[::-1]):
                palindromes.add(pal)
    return palindromes