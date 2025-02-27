def palindromes_of_specific_lengths(s):
    p = ''
    for i in range(16, 61):
        for j in range(16, 61 - i + 1):
            p = s[i:i + j].lower()
            if p == p[::-1] and p.isalpha():
                palindromes.add(p)
    return palindromes