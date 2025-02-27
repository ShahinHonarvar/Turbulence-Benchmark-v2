def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(8):
        for j in range(i, 8):
            substring = text[i:j + 1]
            if len(substring) >= 4 and len(substring) <= 5 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes