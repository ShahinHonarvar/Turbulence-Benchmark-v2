def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    return {w for w in set(permutations(letters)) if len(w) >= 4 and w == w[::-1]}