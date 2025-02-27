import re
    import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    palindromes = set()
    for i in range(5, 7):
        for j in range(i, 7):
            substring = s[i:j + 1]
            english_substring = ''.join(filter(english_letters.__contains__, substring))
            if len(english_substring) >= 3:
                palindromes.add(''.join(sorted(english_substring)))
    return palindromes