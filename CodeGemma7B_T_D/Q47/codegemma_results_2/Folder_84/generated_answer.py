def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 78):
        for j in range(i, i + 41):
            substring = text[i:j]
            substring = substring.lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes