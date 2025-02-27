def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83 - 36):
        for j in range(i + 37, min(i + 61, 84)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes