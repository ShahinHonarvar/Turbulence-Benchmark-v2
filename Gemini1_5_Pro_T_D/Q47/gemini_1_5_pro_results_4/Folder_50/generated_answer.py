def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(36, 93):
        for j in range(i + 10, min(i + 36, 93) + 1):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes