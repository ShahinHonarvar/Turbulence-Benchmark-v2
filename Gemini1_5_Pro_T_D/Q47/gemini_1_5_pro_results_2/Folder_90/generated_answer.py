def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281 - 136):
        for length in range(136, 152):
            substring = text[i:i + length].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(text[i:i + length])
    return palindromes