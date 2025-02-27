def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i + 9, min(i + 51, 301)):
            substring = text[i:j]
            if len(substring) >= 10 and len(substring) <= 50 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes