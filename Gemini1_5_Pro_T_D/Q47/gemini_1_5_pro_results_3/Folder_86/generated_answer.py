def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(30, 96):
        for j in range(i + 33, min(96, i + 55)):
            substring = text[i:j + 1]
            if len(substring) >= 34 and len(substring) <= 55 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes