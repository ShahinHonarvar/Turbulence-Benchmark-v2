def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 61):
        for j in range(i, min(i + 39, 61)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes