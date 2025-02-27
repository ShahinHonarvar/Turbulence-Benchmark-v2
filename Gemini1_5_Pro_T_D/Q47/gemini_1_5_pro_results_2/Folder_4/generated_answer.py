def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 92):
        for j in range(i, 93):
            if 17 <= j - i + 1 <= 66:
                substring = text[i:j + 1].lower()
                if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes