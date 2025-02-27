def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 73):
        for j in range(i + 19, min(i + 56, 73)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes