def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(65, 99 - 25):
        for j in range(26, 34):
            substring = text[i:i + j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes