def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, 10):
            substring = text[i:j]
            if 3 <= len(substring) <= 7 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes