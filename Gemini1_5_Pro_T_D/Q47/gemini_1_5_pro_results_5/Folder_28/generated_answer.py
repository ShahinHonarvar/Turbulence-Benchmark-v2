def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 71):
        for j in range(i + 21, i + 33):
            if j > 71:
                break
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes