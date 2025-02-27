def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 82 - 31):
        for j in range(i + 32, min(i + 35, 83)):
            substring = text[i:j].lower()
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes