def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 89):
        for j in range(i, 89):
            substring = text[i:j + 1]
            if len(substring) >= 12 and len(substring) <= 14 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes