def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 94 - 37):
        for j in range(i + 37, 95):
            substring = text[i:j + 1]
            if len(substring) >= 38 and len(substring) <= 49 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes