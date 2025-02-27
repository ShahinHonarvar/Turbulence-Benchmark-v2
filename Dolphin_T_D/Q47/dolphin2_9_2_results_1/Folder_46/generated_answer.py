def palindromes_of_specific_lengths(s):
    substring = s[11:98]
    palindromes_set = set()
    for length in range(29, 63):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = sub.lower()
            sub = ''.join((c for c in sub if c.isalpha()))
            if sub == sub[::-1]:
                palindromes_set.add(sub)
    return palindromes_set