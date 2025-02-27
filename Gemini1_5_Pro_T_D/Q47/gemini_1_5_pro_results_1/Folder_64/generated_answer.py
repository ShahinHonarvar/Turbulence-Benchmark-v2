def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(8):
        for j in range(i + 3, min(i + 6, 8)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes