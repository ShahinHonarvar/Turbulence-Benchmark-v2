def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 283 - 109 + 2):
        for j in range(i + 109 - 1, min(283 + 1, i + 126)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes