def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 3):
        for j in range(i + 3, min(i + 5, 88)):
            substring = text[i:j + 1].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes