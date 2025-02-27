def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            if len(substring) >= 18 and len(substring) <= 73 and (substring == substring[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes