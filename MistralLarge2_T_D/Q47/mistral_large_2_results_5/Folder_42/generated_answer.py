def palindromes_of_specific_lengths(s):
    s = s[43:96]
    palindromes = set()
    n = len(s)
    for length in range(18, 48):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes