def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 301):
        for j in range(i, min(i + 100, 301)):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) >= 50 and (len(substring) <= 100) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes