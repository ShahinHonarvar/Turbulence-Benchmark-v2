def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 56 - 19):
        for j in range(i + 19, i + 21):
            substring = text[i:j + 1]
            if len(substring) >= 20 and len(substring) <= 21 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes