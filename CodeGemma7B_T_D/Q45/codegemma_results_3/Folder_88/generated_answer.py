def palindromes_between_indices(s):
    return {p for p in permutations(filter(str.isalpha, s[3:8])) if len(p) >= 6 and p == p[::-1]}