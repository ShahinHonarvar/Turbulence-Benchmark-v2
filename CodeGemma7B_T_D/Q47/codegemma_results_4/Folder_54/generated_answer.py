def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i + 18, i + 20):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes