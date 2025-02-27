def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 98 - 39):
        for j in range(40, min(48, 99 - i, i + 1)):
            substring = text[i:i + j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes