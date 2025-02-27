def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 50, min(len(text) + 1, i + 101)):
            substring = text[i:j]
            if substring.isalpha() and len(substring) >= 50 and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes