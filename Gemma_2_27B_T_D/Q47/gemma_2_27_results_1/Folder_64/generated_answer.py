def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(8):
        for j in range(i + 4, min(i + 6, 8)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes