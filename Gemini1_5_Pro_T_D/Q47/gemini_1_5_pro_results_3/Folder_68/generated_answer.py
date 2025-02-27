def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 50, i + 101):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes