def palindromes_of_specific_lengths(s):
    s = s[70:141]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(3, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes