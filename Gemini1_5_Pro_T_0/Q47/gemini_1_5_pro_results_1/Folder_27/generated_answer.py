def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 99 - 25):
        for j in range(i + 26, i + 30):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes