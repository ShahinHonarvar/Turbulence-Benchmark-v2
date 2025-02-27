def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(8):
        for j in range(i + 1, min(i + 6, 9)):
            substring = text[i:j].lower()
            if 4 <= len(substring) <= 5 and substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes