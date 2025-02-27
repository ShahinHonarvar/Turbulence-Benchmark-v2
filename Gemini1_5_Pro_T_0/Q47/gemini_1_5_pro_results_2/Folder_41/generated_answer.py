def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 2, min(i + 5, 8)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes