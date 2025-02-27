def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 292):
        for j in range(i + 153, min(i + 182, 293) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes