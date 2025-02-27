def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i + 1, 61):
            substring = text[i:j]
            if 18 <= len(substring) <= 36 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes