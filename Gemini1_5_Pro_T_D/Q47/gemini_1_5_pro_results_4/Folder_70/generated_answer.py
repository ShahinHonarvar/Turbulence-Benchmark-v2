def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 70):
        for j in range(i + 24, min(i + 53, 71)):
            substring = text[i:j]
            if len(substring) >= 24 and len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes