def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, min(i + 81, len(text) + 1)):
            substring = text[i:j]
            if len(substring) >= 5 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes