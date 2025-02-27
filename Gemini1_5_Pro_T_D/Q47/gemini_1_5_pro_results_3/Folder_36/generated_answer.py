def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 283 - 115 + 2):
        for j in range(115, min(135, 284 - i, i + 1)):
            substring = text[i:i + j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:i + j])
    return palindromes