def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(43, 95 - 17):
        for j in range(i + 17, 96):
            substring = text[i:j + 1]
            if len(substring) >= 18 and len(substring) <= 47:
                if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes