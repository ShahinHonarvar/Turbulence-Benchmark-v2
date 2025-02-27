def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(20, 75):
        for j in range(i + 1, 75):
            substring = text[i:j + 1]
            if 36 <= len(substring) <= 42 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes