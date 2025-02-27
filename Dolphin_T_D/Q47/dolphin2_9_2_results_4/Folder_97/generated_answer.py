def palindromes_of_specific_lengths(s):
    s = s[27:95]
    palindromes_set = set()
    for length in range(38, 50):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes_set.add(substring)
    return palindromes_set