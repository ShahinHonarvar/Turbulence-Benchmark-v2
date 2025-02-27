def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(20, 75):
        for j in range(36, 43):
            if i + j <= 75:
                substring = text[i:i + j].lower()
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes