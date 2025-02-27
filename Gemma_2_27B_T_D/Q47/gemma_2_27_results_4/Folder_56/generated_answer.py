def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 10):
        for j in range(i + 2, min(i + 8, 10)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes