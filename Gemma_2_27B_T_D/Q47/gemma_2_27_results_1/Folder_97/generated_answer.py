def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 95):
        for j in range(i + 38, min(i + 50, 95)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes