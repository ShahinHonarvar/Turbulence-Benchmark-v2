def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i + 18, min(i + 20, 78)):
            substring = text[i:j]
            if len(substring) >= 18 and len(substring) <= 19 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes