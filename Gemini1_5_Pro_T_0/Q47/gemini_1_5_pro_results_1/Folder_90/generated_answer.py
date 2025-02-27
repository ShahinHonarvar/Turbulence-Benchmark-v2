def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281 - 136):
        for j in range(i + 136, min(281, i + 152)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes