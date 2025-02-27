def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(3, 301):
        for j in range(i, 301):
            substring = text[i - 1:j].lower()
            if substring.isalpha() and substring == substring[::-1] and (30 <= len(substring) <= 300):
                palindromes.add(text[i - 1:j])
    return palindromes