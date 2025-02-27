def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i + 25, min(i + 31, 86)):
            substring = text[i:j + 1]
            if len(substring) >= 26 and len(substring) <= 31 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes