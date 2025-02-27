def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i + 18, min(i + 37, 60)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes