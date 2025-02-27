def palindromes_between_indices(s):
    english_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(1, min(7, len(s)) + 1):
        for j in range(i, min(7, len(s)) + 1):
            substring = s[i - 1:j].lower()
            if len(substring) >= 3 and substring == substring[::-1] and all((char in english_lowercase for char in substring)):
                palindromes.add(substring)
    return palindromes