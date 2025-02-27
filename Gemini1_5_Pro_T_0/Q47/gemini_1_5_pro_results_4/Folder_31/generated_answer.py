def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83 - 36):
        for j in range(37, min(61, 84 - i, i + 1)):
            substring = text[i:i + j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes