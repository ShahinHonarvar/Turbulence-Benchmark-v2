def palindromes_between_indices(s):
    palindromes = set()
    substring = s[4:6]
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            for k in map(str.lower, substring):
                if str(k) == str(k)[::-1]:
                    palindromes.add(k)
    return palindromes