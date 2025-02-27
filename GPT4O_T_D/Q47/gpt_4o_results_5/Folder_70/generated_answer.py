def palindromes_of_specific_lengths(s):
    s = s[10:71]
    s = ''.join(filter(str.isalpha, s))
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 24, min(i + 53, len(s) + 1)):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(s[i:j])
    return palindromes