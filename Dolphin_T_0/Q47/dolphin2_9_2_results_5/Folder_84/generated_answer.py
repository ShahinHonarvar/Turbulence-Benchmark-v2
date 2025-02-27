def palindromes_of_specific_lengths(string):
    s = string[23:77]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes