def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 7):
        for j in range(i, 7):
            substring = s[i - 1:j].lower()
            if all((char in english_letters for char in substring)) and len(substring) >= 4 and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes