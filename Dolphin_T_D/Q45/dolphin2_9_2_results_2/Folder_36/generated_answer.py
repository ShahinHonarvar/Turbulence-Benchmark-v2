def palindromes_between_indices(string):
    substring = string[5:9]
    english_letters = ''.join((ch for ch in substring if ch.isalpha()))
    if len(english_letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 2, len(english_letters) + 1):
            portion = english_letters[i:j]
            if portion == portion[::-1]:
                palindromes.add(portion)
    return palindromes