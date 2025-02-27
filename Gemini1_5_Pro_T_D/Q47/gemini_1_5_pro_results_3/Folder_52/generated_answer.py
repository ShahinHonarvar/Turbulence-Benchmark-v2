def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(44, 100):
        for j in range(i + 13, min(100, i + 43)):
            substring = text[i:j]
            if len(substring) >= 13 and len(substring) <= 42 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes