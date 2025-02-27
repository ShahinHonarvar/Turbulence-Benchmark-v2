def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(34, 91):
        for j in range(14, 40):
            if i + j - 1 > len(s) - 1:
                continue
            substring = s[i:i + j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes