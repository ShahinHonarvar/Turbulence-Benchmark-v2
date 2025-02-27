def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    return {s.lower() for s in set(itertools.permutations(s[:8])) if is_palindrome(s) and len(s) >= 6}