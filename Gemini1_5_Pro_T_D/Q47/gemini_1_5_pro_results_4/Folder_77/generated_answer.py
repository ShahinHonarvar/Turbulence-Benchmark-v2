def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(103, 277):
        for j in range(i + 100, min(i + 170, 277)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes