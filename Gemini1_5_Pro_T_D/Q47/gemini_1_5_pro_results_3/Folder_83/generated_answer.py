def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(75, 96):
        for j in range(i + 7, min(i + 10, 96)):
            substring = text[i:j]
            if len(substring) >= 7 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes