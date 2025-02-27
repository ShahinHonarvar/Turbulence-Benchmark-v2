def palindromes_between_indices(s):
    s = s[2:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(4, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes