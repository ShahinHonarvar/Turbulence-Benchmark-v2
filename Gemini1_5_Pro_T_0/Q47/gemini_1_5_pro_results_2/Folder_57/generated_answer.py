def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 39, min(i + 53, 95)):
            substring = text[i:j]
            if len(substring) >= 39 and len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes