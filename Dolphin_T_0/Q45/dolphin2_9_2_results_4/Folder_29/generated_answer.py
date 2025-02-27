import string

def palindromes_between_indices(s):
    letters = set(s[2:10].lower())
    n = len(s[2:10])
    if n < 6:
        return set()
    PALINDROMES = set()

    def dfs(l, r, pal):
        if l > r:
            if len(pal) >= 6 and pal == pal[::-1]:
                PALINDROMES.add(pal)
            return
        for c in letters:
            dfs(l + 1, r, pal + c)
            dfs(l, r - 1, c + pal)
    dfs(0, n - 1, '')
    return PALINDROMES