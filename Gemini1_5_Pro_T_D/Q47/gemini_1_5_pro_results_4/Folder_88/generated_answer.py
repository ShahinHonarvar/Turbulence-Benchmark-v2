def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 2):
        for j in range(4, 6):
            if i + j <= 87 + 1:
                substring = text[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes