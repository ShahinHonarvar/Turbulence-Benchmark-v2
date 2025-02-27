def palindromes_of_specific_lengths(text):
    text = ''.join((c for c in text.lower() if c.isalpha()))
    palindromes = set()
    for i in range(31, 92):
        for j in range(i, 92):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes