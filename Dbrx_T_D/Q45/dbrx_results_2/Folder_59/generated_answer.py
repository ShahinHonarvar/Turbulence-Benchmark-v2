import re
    from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chars_between_indices = set(s[8:10]) & english_letters
    if not chars_between_indices:
        return set()
    result = set()
    for c in chars_between_indices:
        for i in range(1, 4):
            for j in range(1, 4):
                sub_s = s[8:10]
                sub_s = re.sub(c, '', sub_s, flags=re.IGNORECASE)
                sub_s = ''.join(sorted(sub_s))
                sub_s = ''.join((c for c in sub_s if c not in ('', ' ', '\n')))
                if len(sub_s) == i + j - 2:
                    sub_s = ''.join([c] * i + [c] + [c] * j)
                    if is_palindrome(sub_s):
                        result.add(sub_s)
    return result