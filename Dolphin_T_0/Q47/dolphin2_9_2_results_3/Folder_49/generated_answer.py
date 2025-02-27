def palindromes_of_specific_lengths(s):
    s = s[10:101]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring.lower())):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring.lower())
    return palindromes