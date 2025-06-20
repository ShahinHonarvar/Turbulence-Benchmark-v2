def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 101):
        for j in range(i, min(i + 50, 101)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes