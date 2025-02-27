def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 98 - 5):
        for length in range(6, 10):
            substring = text[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha() and (len(substring) == length):
                palindromes.add(substring)
    return palindromes