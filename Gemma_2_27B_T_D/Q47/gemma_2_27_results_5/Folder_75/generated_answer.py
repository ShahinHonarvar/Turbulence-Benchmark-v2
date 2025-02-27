def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 75):
        for j in range(i + 23, min(i + 40, 75)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes