def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 95 - 57 + 2):
        for j in range(i + 57, min(i + 61, 96)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes