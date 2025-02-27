def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 88):
        for j in range(i + 38, min(i + 61, 88)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes