def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 42, min(i + 47, 78)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes