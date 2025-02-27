def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 76):
        for j in range(i, 76):
            substring = text[i:j + 1]
            if 10 <= len(substring) <= 20 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes