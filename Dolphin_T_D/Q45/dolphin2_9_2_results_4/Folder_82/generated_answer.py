def palindromes_between_indices(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = ''.join(filter(str.isalpha, s[1:7]))
    s = s.lower()
    return set(filter(is_palindrome, set(''.join(permutations(s)))))