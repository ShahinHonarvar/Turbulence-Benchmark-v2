def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(36, 93):
        for j in range(i + 10, i + 36):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes