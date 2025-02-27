def palindromes_of_specific_lengths(s):
    s = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length])
    return palindromes