def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s[0:6]))
    return set(filter(lambda x: len(x) >= 4 and is_palindrome(x), set((''.join(p) for p in permutations(s.lower())))))