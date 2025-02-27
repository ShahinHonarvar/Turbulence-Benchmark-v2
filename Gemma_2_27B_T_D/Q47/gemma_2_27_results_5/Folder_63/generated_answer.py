def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i + 26, min(i + 31, 86)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes