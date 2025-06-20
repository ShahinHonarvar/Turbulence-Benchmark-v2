def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 300):
        for j in range(i + 2, min(i + 10, 301)):
            substring = text[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes