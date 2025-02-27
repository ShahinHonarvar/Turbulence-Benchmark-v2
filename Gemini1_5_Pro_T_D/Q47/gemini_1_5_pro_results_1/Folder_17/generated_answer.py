def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 95 + 1 - 52):
        for j in range(i + 52 - 1, i + 55):
            substring = text[i:j + 1]
            if len(substring) >= 52 and len(substring) <= 55:
                if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes