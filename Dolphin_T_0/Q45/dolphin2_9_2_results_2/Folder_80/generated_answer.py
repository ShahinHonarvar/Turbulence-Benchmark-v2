def palindromes_between_indices(s):
    if s[2] == s[3] == s[4] == s[5] == s[6] == s[7] == s[8] == s[9]:
        return set()
    palindromes = set()
    for p in [''.join(p) for p in permutations(s[3:9]) if len(set(p)) == len(s[3:9])]:
        if len(p) >= 7 and p == p[::-1]:
            palindromes.add(p.lower())
    return palindromes