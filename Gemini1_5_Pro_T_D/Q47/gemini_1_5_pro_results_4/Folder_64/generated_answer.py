def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(8):
        for j in range(i + 1, min(i + 6, 8)):
            substring = text[i:j]
            if 4 <= len(substring) <= 5 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes