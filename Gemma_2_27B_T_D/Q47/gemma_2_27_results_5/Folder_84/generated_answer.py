def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 78):
        for j in range(i, 78):
            substring = text[i:j + 1]
            if len(substring) >= 13 and len(substring) <= 40 and (substring.lower() == substring.lower()[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes