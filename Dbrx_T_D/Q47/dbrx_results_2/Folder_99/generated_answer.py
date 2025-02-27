def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(119, 142):
        for start in range(127 - length, 288 - length + 2):
            if s[start:start + length] == s[start:start + length][::-1]:
                palindromes.add(s[start:start + length])
    return palindromes