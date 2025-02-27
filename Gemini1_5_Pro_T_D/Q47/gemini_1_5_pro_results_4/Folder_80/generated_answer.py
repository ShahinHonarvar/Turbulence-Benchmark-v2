def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(35, 89):
        for j in range(i + 23, min(89, i + 33)):
            substring = text[i:j + 1]
            if len(substring) >= 24 and len(substring) <= 33 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes