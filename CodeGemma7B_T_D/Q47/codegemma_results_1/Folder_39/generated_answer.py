def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i + 50, i + 54):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes