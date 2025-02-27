def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 98 - 30):
        for j in range(i + 31, min(99, i + 52)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes