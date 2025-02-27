def palindromes_of_specific_lengths(s):
    s = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes