def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 76):
        for j in range(i + 10, min(i + 21, 76)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes