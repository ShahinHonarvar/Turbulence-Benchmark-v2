def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i + 49, i + 53):
            if j <= 91:
                substring = text[i:j + 1]
                if len(substring) >= 50 and len(substring) <= 53:
                    if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                        palindromes.add(substring)
    return palindromes