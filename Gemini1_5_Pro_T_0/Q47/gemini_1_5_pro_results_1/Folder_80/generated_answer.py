def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(35, 88 - 23):
        for j in range(i + 23, 89):
            substring = text[i:j + 1]
            if len(substring) >= 24 and len(substring) <= 33 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes