def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 99):
        for j in range(i + 5, min(i + 10, 99)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes