def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(7):
        for j in range(i + 2, min(i + 7, 7)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes