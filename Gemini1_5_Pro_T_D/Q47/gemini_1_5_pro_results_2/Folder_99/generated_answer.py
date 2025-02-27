def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 288 - 119 + 2):
        for j in range(i + 119 - 1, min(288 + 1, i + 141)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes