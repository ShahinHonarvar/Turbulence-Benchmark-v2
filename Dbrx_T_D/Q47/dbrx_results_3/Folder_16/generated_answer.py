def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[15:87]
    palindromes = set()
    for i in range(len(s) - 50):
        for length in range(51, 61):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes