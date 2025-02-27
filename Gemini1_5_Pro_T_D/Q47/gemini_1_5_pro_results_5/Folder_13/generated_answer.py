def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 96):
        for j in range(i + 57, i + 61):
            if j > 95:
                continue
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes