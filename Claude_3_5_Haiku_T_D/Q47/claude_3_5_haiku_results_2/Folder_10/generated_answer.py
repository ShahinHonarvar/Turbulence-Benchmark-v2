def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for length in range(16, 40):
        for start in range(16, 61 - length + 1):
            substring = text[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes