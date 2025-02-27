def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(10, 37):
        for start in range(24, len(s) - length + 2):
            if s[start:start + length] == s[start:start + length][::-1]:
                palindromes.add(s[start:start + length])
    return palindromes