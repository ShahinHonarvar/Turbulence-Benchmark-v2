def palindromes_between_indices(s):
    substring = s[1:6]
    palindromes = set()
    for i in range(4, len(substring) + 1):
        substrings = itertools.combinations(substring, i)
        for sub in substrings:
            sub = ''.join(sub)
            if sub == sub[::-1] and len(sub) >= 4:
                palindromes.add(sub.lower())
    if len(palindromes) == 0:
        return set()
    else:
        return palindromes