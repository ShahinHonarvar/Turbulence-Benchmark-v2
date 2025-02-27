def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 201):
        for j in range(5, 11):
            if i + j <= 201:
                substring = text[i:i + j]
                if substring.isalpha() and len(substring) == j and (substring.lower() == substring[::-1].lower()):
                    palindromes.add(substring.lower())
    return palindromes