def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for length in range(50, 101):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes