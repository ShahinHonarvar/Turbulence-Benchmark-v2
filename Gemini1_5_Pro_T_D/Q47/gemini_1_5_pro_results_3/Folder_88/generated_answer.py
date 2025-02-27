def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 3):
        for j in range(4, 6):
            if i + j <= 88:
                substring = text[i:i + j].lower()
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes