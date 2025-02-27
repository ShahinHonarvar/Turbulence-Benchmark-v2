def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s[11:96]))
    s = s.lower()
    lengths = range(45, 53)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.upper())
    return palindromes