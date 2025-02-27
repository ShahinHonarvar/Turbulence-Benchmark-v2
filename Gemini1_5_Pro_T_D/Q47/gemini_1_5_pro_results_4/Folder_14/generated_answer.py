def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 74):
        for j in range(i + 6, min(i + 9, 75)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes