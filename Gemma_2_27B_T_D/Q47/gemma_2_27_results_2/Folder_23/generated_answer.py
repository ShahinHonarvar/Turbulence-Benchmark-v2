def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            if len(substring) >= 17 and len(substring) <= 55 and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes