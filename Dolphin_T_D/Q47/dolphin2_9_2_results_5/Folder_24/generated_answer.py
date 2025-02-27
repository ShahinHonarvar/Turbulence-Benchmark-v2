def palindromes_of_specific_lengths(s):
    s = s[12:93]
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring.lower())):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring.lower())
    return palindromes