def palindromes_of_specific_lengths(s):
    substr = s[12:100]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes