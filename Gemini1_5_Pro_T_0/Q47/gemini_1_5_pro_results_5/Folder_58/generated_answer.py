def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 283 - 109 + 2):
        for j in range(109, min(127, 284 - i, i - 124) + 1):
            substring = text[i:i + j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes