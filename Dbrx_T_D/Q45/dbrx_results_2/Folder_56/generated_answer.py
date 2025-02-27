from string import ascii_letters
    import re

def palindromes_between_indices(s):
    english_letters = ascii_letters
    substring = s[5:10].lower()
    palindromes = set()
    for i in range(len(substring) - 4):
        for j in range(i + 1, len(substring) - 3):
            candidate = substring[i] + substring[j:]
            if candidate == candidate[::-1] and re.fullmatch(f'[{english_letters}]*', candidate):
                palindromes.add(candidate)
    return palindromes