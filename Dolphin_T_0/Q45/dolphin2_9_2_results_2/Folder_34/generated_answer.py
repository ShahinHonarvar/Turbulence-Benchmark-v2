from string import ascii_lowercase

def palindromes_between_indices(s):

    def perms(s):
        if len(s) == 1:
            return set(s)
        else:
            permutations = set()
            for i, letter in enumerate(s):
                for permutation in perms(s[:i] + s[i + 1:]):
                    permutations.add(letter + permutation)
            return permutations

    def is_palindrome(s):
        return s == s[::-1]
    return {p.lower() for p in perms(s[5:8]) if is_palindrome(p) and len(p) >= 4}