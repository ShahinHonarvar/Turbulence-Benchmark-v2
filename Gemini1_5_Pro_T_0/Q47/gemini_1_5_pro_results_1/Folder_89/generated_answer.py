def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 89):
        for j in range(i + 11, min(i + 15, 89)):
            substring = text[i:j]
            if len(substring) >= 12 and len(substring) <= 14 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes