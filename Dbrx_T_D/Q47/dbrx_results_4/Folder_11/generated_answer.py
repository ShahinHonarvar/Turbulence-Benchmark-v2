def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(24, 98):
        for j in range(10, 37):
            if i + j - 1 <= 97 and s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes