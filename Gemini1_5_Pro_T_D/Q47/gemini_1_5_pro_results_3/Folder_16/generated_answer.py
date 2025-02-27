def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 87):
        for j in range(i + 51, min(i + 61, 87)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes