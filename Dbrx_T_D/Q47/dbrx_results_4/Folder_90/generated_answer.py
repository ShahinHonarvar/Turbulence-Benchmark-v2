def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(106, 281):
        for j in range(136, 152):
            if i + j - 1 <= len(s) and s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes