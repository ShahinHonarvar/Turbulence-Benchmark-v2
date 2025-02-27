def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(3, 8):
        for start in range(1, 10 - length + 1):
            if s[start - 1:start + length - 1] == s[start - 1:start + length - 1][::-1]:
                palindromes.add(s[start - 1:start + length - 1])
    return palindromes