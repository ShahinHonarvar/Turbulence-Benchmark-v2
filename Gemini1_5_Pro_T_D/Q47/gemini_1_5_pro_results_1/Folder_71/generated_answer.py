def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 65 - 22):
        for j in range(i + 23, min(i + 37, 66)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes