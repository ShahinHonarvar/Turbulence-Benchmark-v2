def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(14, 91):
        for j in range(i + 55, min(i + 72, 91)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes