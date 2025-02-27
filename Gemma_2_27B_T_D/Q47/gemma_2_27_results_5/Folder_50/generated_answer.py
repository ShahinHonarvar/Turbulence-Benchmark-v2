def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(36, 93):
        for j in range(i, 93):
            substring = text[i:j + 1]
            if len(substring) >= 10 and len(substring) <= 35 and (substring == substring[::-1]) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes