def palindromes_of_specific_lengths(s):
    s = s[10:84]
    palindromes = set()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if len(set(sub.lower()) - set('abcdefghijklmnopqrstuvwxyz')) == 0 and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes