def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i + 18, min(i + 37, len(text) + 1)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes