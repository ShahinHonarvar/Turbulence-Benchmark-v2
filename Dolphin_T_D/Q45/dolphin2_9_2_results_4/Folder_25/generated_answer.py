def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s))
    substring = s[1:4]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes