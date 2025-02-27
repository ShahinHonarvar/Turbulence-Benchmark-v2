def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 300):
        for j in range(i + 2, 301):
            substring = text[i:j].lower()
            if substring == substring[::-1] and len(substring) in range(3, 11) and substring.isalpha():
                palindromes.add(substring)
    return palindromes