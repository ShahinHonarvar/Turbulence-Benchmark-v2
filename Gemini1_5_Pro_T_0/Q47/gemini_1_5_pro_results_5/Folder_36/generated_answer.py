def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(i + 114, min(284, i + 134) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(text[i:j])
    return palindromes