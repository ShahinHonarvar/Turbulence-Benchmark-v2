def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(6):
        for j in range(3, 6):
            if i + j - 1 < len(s) and s[i:j + i] == s[i:j + i][::-1]:
                palindromes.add(s[i:j + i])
    return palindromes