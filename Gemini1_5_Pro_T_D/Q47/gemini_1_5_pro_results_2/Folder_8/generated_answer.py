def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 72 - 49):
        for length in range(50, 52):
            substring = text[i:i + length + 1].lower()
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes