def palindromes_between_indices(s):
    chars = [c.lower() for c in s if c.isalpha() and 0 <= s.index(c) <= 4]
    if len(set(chars)) < 4:
        return set()

    def create_palindromes(s):
        if len(s) >= 4 and s == s[::-1]:
            return set(s)
        if len(s) < 4 or len(set(s)) < 4:
            return set()
        return set.union(*[create_palindromes(s[i + 1:]) for i in range(len(s) - 1)])
    return create_palindromes(''.join(chars))