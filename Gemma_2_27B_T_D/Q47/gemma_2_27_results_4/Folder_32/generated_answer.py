def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 43, i + 48):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes