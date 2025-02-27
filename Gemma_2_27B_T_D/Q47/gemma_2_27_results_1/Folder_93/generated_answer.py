def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 96):
        for j in range(i, 96):
            substring = text[i:j + 1].lower()
            if len(substring) >= 13 and len(substring) <= 49 and (substring == substring[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes