def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 71):
        for j in range(24, 53):
            if i + j <= 71:
                substring = text[i:i + j].lower()
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes