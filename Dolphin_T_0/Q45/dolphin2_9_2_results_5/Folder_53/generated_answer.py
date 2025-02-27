def palindromes_between_indices(s):

    def is_palindrome(t):
        return t == t[::-1]
    indices = range(4, 9)
    letters = set((c.lower() for c in s if c.isalpha()))
    return set((s[i] + s[j] + s[k] + s[l] + s[m] + s[n] for i in indices for j in indices for k in indices for l in indices for m in indices for n in indices if s[i] != s[j] != s[k] != s[l] != s[m] != s[n] and is_palindrome(s[i] + s[j] + s[k] + s[l] + s[m] + s[n]) and (set([s[i], s[j], s[k], s[l], s[m], s[n]]) <= letters)))