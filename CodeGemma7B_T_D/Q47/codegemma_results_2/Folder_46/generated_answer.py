def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 97):
        for j in range(i + 29, i + 62 + 1):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes