def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower().strip()
    for i in range(28, 95):
        for j in range(i + 37, i + 50):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes