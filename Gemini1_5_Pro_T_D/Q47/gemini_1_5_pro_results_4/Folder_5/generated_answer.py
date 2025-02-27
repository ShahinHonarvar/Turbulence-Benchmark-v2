def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(63, 67):
        for j in range(i + 3, min(71, i + 5)):
            substring = text[i:j + 1]
            if len(substring) >= 4 and len(substring) <= 5 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes