def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(35, 89):
        for j in range(i + 23, min(89, i + 33)):
            substring = text[i:j]
            if len(substring) >= 24 and len(substring) <= 33 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes