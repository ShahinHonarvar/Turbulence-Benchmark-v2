def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 77):
        for j in range(i + 13, min(i + 41, 78)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes