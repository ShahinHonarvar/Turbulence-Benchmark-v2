def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i, 96):
            if 20 <= j - i + 1 <= 66:
                substring = text[i:j + 1]
                if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes