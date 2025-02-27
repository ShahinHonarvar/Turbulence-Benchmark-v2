def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 95 - 51):
        for length in range(52, 56):
            substring = text[i:i + length]
            if len(substring) == length and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes