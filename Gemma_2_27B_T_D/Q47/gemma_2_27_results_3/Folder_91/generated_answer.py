def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11):
        for j in range(i, min(i + 6, 11)):
            substring = text[i:j + 1]
            if len(substring) in range(3, 6) and substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes