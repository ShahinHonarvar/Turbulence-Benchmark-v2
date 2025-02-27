def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for i in range(200, 301):
        for j in range(i, 0, -1):
            substring = text[j:i + 1]
            if substring == substring[::-1] and len(substring) in range(10, 51):
                palindromes.add(substring)
    return palindromes