def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11):
        for j in range(i + 1, min(len(s), 11)):
            substring = s[i:j + 1].lower()
            if 3 <= len(substring) <= 5 and substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes