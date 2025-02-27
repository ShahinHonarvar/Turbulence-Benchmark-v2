def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    a = [c.lower() for c in s if c.isalpha()][:7]
    return {''.join(p) for p in itertools.product(*[a] * 2) if is_palindrome(p) and len(p) >= 4}