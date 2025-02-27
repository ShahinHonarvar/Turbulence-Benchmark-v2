def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 80):
        for j in range(i + 35, i + 42):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes