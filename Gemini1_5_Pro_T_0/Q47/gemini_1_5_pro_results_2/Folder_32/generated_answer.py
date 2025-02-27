def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 42, min(i + 47, 78)):
            substring = text[i:j + 1]
            if len(substring) >= 43 and len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes