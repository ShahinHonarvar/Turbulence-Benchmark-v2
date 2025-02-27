def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i + 20, min(i + 67, 96)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(text[i:j])
    return palindromes