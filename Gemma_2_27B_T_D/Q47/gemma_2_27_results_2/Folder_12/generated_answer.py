def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(62, 89):
        for j in range(i + 18, min(i + 22, 89)):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes