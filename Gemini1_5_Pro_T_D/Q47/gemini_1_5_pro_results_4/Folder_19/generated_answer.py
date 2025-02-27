def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 49):
        for j in range(i + 3, min(i + 8, 56)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes