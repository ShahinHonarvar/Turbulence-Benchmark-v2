def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 38, min(95, i + 52) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes