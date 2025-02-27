def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83):
        for j in range(i + 13, min(84, i + 67)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes