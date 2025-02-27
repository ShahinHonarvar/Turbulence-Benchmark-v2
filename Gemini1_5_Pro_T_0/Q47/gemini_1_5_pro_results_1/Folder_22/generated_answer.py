def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 201):
        for j in range(i + 5, min(i + 11, 201)):
            substring = text[i:j]
            if len(substring) >= 5 and len(substring) <= 10 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes