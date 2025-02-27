def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 51):
        for j in range(3, 8):
            if i + j <= 56:
                substring = text[i:i + j].lower()
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes