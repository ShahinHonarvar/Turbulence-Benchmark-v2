def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 99):
        for j in range(i + 5, min(i + 10, 99)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes