def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 301):
        for j in range(i, min(i + 100, 301)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha() and (50 <= len(substring) <= 100):
                palindromes.add(substring)
    return palindromes