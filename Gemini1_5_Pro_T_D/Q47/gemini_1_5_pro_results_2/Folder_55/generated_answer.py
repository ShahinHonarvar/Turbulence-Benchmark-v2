def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 66):
        for j in range(i + 9, min(76, i + 11)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(text[i:j])
    return palindromes