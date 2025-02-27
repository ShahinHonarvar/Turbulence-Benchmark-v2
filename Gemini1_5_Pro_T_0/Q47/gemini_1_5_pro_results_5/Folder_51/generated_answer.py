def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, min(i + 4, 9)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes