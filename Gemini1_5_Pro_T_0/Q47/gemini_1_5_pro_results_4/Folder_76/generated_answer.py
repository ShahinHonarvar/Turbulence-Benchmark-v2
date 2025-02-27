def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 292 - 153):
        for j in range(i + 154, min(i + 183, 293)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes