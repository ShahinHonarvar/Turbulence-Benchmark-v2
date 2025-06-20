def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 79):
        for j in range(i + 35, min(i + 42, 80)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes