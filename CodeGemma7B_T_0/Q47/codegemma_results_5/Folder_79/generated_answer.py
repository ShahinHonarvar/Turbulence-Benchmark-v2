def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 1, 9):
            for k in range(i, j + 1):
                substring = text[i:j + 1]
                if substring == substring[::-1] and len(substring) in range(3, 5):
                    palindromes.add(substring)
    return palindromes