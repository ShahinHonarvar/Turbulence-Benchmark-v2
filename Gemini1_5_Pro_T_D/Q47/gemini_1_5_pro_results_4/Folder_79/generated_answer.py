def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 2, min(i + 4, 8) + 1):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes