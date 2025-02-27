def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 94 - 38):
        for j in range(i + 39, min(i + 53, 95)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes