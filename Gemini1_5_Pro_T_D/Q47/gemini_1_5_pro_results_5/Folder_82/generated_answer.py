def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(3, 301):
        for j in range(i, 301):
            substring = text[i:j + 1]
            if 30 <= len(substring) <= 300 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes