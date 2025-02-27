from collections import defaultdict

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    if len(s) < 85:
        return palindromes
    for i in range(33, 86 - 26 + 1):
        for j in range(26, 31 + 1):
            if i + j - 1 > len(s):
                break
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes