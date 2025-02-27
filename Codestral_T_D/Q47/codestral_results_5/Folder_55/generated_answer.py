def palindromes_of_specific_lengths(s):
    s = s[10:76]
    s = ''.join(filter(str.isalpha, s)).lower()
    l = len(s)
    palindromes = set()
    for length in range(10, 21):
        for i in range(l - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes