def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(5):
        for j in range(i + 3, min(i + 5, 5)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes