from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    valid_chars = [c.lower() for c in s[6:10] if c.isalpha()]
    result = set()
    char_count = Counter(valid_chars)

    def backtrack(path, count):
        if len(path) >= 3 and is_palindrome(path):
            result.add(path)
        for char in char_count:
            if count[char] > 0:
                count[char] -= 1
                backtrack(path + char, count)
                count[char] += 1
    backtrack('', char_count.copy())
    return result