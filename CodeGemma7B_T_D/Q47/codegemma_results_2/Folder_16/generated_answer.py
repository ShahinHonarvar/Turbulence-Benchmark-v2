def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 87):
        for j in range(i, 87):
            substring = text[i:j + 1]
            if substring == substring[::-1] and 50 < len(substring) <= 60:
                palindromes.add(substring)
    return palindromes