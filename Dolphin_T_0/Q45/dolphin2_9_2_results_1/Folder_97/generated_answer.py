def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substrings = set((''.join(p) for i in range(3, 6) for p in itertools.permutations(s[:i], i)))
    palindromes = {s for s in substrings if len(s) >= 3 and is_palindrome(s.lower())}
    return palindromes