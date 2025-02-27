def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i, 293):
            if 154 <= j - i + 1 <= 182:
                substring = text[i:j + 1]
                if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes