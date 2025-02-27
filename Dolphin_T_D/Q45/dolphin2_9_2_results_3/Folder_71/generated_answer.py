def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join((c for c in s.lower() if c.isalpha()))
    if len(s) >= 4:
        s = s[1:4]
        if s == '':
            while len(s) < 4:
                s += s[0]
        if is_palindrome(s):
            chars = [c for c in s]
            chars.sort()
            result = {s}
            for perm in set(map(''.join, permutations(chars))):
                if len(perm) >= 4 and is_palindrome(perm):
                    result.add(perm)
            return result
    return set()