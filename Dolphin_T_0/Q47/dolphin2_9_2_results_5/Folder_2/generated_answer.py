def palindromes_of_specific_lengths(s):
    s = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length])
    return palindromes