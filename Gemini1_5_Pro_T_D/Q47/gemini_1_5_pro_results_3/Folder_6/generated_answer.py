def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 95):
        for j in range(i + 40, min(i + 48, 99)):
            substring = text[i:j]
            if len(substring) >= 40 and len(substring) <= 47 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes