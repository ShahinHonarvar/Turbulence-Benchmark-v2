def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 3):
        for j in range(4, 6):
            if i + j <= 88:
                substring = text[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes