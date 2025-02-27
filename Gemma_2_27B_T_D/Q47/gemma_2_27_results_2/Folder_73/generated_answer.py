def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21, 63):
        for j in range(i + 22, min(i + 34, 63)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(text[i:j])
    return palindromes