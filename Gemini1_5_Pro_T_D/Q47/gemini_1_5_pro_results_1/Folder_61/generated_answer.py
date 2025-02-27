def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31):
        for j in range(i, 31):
            substring = text[i:j + 1].lower()
            if len(substring) >= 20 and len(substring) <= 30 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes