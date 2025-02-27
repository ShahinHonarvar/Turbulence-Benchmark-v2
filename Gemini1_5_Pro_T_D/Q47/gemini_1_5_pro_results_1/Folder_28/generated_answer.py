def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 71 - 20):
        for j in range(i + 21, min(72, i + 33)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes