def palindrome_of_length_at_least_n(s):
    return {w for w in set(''.join((c for c in s if c.isalpha())).lower().split()) if len(w) >= 112 and w == w[::-1]}