def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 45, min(i + 101, 51)):
            substring = text[i:j + 1]
            if len(substring) >= 50 and len(substring) <= 100 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes