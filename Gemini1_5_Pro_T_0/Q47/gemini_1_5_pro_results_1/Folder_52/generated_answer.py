def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(44, 99 - 13 + 1):
        for j in range(i + 13, min(100, i + 42) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes