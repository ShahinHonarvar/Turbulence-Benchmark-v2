def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 65 - 22):
        for j in range(i + 23, 66):
            substring = text[i:j]
            if len(substring) >= 23 and len(substring) <= 36 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes