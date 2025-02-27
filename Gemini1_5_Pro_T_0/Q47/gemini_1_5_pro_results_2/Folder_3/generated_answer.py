def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 95 - 48):
        for length in range(49, 52):
            substring = text[i:i + length].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes