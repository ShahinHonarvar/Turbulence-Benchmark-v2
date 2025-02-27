def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(14, 91):
        for j in range(i + 55, min(i + 72, 91)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes