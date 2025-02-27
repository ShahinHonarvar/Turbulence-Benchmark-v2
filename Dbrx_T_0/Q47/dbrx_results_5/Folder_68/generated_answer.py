def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(50, 101):
        for start in range(51 - length):
            if s[start:start + length] == s[start:start + length][::-1]:
                palindromes.add(s[start:start + length])
    return palindromes