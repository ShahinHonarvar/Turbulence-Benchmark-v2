def palindromes_between_indices(text):
    palindromes = set()
    for i in range(6, 10):
        for j in range(i - 1, -1, -1):
            substring = text[j:i + 1].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes