def palindromes_of_specific_lengths(s):
    s = s[13:100]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(s) - length + 1):
            t = s[i:i + length]
            if t.lower() == t.lower()[::-1]:
                palindromes.add(t)
    return palindromes