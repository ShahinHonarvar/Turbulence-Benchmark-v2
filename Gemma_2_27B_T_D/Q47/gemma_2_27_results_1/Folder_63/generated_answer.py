def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i + 26, min(i + 32, 86)):
            substring = text[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes