def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i, min(i + 50, 301)):
            substring = text[i:j + 1]
            if len(substring) >= 10 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes