def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i, 301):
            substring = text[i:j + 1].lower()
            if len(substring) >= 10 and len(substring) <= 50 and (substring == substring[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes