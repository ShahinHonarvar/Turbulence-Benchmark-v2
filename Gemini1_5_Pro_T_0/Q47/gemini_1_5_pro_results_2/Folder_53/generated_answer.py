def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 300):
        for j in range(i + 2, min(i + 10, 300) + 1):
            substring = text[i:j]
            if len(substring) >= 3 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes