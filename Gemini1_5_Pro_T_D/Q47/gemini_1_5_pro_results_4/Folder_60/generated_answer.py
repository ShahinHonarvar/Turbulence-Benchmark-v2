def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 82 - 31):
        for length in range(32, 35):
            substring = text[i:i + length].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes