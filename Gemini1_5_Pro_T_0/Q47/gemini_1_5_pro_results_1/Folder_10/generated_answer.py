def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 45):
        for j in range(61 - i):
            substring = text[j + 16:j + i + 16]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes