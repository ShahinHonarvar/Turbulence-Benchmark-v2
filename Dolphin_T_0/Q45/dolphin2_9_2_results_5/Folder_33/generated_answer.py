def palindromes_between_indices(string):
    sub_string = string[6:10]
    palindromes = set()
    sub_len = len(sub_string)
    if sub_len < 4:
        return palindromes
    for i in range(4, sub_len + 1):
        for comb in combinations(sub_string, i):
            s = ''.join(sorted(comb))
            if not s == s[::-1]:
                continue
            palindromes.add(s.lower())
    return palindromes