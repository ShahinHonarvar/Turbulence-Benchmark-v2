def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(40, 95):
        for j in range(i + 45, min(i + 52, 95 + 1)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes