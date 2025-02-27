def palindromes_between_indices(s):
    substr = ''.join((c.lower() for c in s[4:8] if c.isalpha()))
    if len(substr) < 2:
        return set()

    def palindromes(s):
        if len(s) <= 1:
            return set(s)
        else:
            return {s[0] + c + s[0] for c in palindromes(s[1:])} | palindromes(s[1:])
    return palindromes(substr)