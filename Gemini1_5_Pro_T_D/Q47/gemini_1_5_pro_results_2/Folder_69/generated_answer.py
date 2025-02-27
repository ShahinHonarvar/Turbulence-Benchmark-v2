def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 96 - 44):
        for j in range(45, 53):
            if i + j <= 97:
                substring = text[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(text[i:i + j])
    return palindromes