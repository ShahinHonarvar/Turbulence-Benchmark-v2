def palindromes_of_specific_lengths(s):
    s = s[29:99]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes