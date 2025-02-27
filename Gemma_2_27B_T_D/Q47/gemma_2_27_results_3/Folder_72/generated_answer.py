def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 91):
        for j in range(i + 27, min(i + 59, 91)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes