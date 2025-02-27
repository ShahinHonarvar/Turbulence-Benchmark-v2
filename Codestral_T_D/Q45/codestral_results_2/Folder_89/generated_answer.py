from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[5:10].lower()
    palindromes = set((p for i in range(6, len(s) + 1) for p in permutations(s, i) if is_palindrome(''.join(p))))
    return palindromes