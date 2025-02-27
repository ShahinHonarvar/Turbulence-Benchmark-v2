def palindromes_of_specific_lengths(s):
    s = s[15:96]
    palindromes = set()
    for i in range(20, 67):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes