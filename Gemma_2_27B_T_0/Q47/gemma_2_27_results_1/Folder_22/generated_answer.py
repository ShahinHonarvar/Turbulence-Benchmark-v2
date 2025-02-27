def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 201):
        for j in range(i, min(i + 10, 201)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and len(substring) in range(5, 11) and substring.isalpha():
                palindromes.add(substring)
    return palindromes