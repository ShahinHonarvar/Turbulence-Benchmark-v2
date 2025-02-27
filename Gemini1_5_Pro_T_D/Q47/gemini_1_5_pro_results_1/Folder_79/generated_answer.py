def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 2, min(i + 5, 9)):
            substring = text[i:j + 1]
            if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes