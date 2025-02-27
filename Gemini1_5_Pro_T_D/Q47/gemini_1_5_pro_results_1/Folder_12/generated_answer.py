def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 88 - 17):
        for j in range(i + 17, min(89, i + 22)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes