def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 88):
        for j in range(i + 4, i + 6):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes