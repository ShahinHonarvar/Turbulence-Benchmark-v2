def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 98 - 31 + 2):
        for j in range(i + 31, min(i + 51, 99) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes