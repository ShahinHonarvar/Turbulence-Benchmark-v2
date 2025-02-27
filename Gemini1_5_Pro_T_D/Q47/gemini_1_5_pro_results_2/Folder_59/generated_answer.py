def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101):
        for j in range(i + 3, min(i + 16, 101)):
            substring = text[i:j]
            if len(substring) >= 3 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes