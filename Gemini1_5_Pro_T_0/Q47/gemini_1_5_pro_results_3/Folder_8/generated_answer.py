def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 72 - 49):
        for length in range(50, 52):
            substring = text[i:i + length + 1]
            if len(substring) == length + 1 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes