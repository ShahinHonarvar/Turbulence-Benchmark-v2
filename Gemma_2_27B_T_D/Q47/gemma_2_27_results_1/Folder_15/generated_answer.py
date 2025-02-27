def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(7):
        for j in range(i, 7):
            substring = text[i:j + 1]
            if len(substring) in range(3, 7) and substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes