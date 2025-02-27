import re
from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def extend_palindrome(palindrome, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            palindrome = s[left] + palindrome + s[right]
            left -= 1
            right += 1
        return palindrome

    def find_palindromes():
        chars = defaultdict(int)
        for c in s[6:10]:
            chars[c.lower()] += 1
        for c in chars:
            if chars[c] >= 3:
                palindrome = c * chars[c]
                yield palindrome
                if chars[c] >= 4:
                    palindrome = c * (chars[c] // 2)
                    yield extend_palindrome(palindrome, chars[c] // 2 - 1, chars[c] // 2 + 1)
                if chars[c] >= 5:
                    palindrome = c * (chars[c] // 2)
                    yield extend_palindrome(palindrome, chars[c] // 2 - 2, chars[c] // 2 + 2)
    return set(find_palindromes())