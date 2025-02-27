def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 95 - 51):
        for j in range(i + 52, min(i + 56, 96)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes