def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i + 28, min(i + 62, 98) + 1):
            substring = text[i:j]
            if len(substring) >= 29 and len(substring) <= 62 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes