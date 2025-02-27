def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 98 - 5):
        for j in range(i + 5, min(99, i + 10)):
            substring = text[i:j]
            if len(substring) >= 6 and len(substring) <= 9 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes