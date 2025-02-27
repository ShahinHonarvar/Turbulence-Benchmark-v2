def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 79):
        for j in range(i + 35, min(i + 42, 80)):
            substring = text[i:j]
            if len(substring) >= 35 and len(substring) <= 41 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes