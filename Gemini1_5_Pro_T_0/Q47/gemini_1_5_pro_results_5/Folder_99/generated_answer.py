def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 288 - 118):
        for j in range(i + 119, min(i + 142, 289)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes