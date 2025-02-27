from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]

    def get_arrangements(s):
        if len(s) == 1:
            return [s]
        arrs = []
        for i in range(len(s)):
            char = s[i]
            rest = s[:i] + s[i + 1:]
            for arr in get_arrangements(rest):
                arrs.append(char + arr)
        return arrs
    relevant_chars = s[2:6].lower()
    arrangements = get_arrangements(relevant_chars)
    palindromes = [arr for arr in arrangements if is_palindrome(arr) and len(arr) >= 5]
    return set(palindromes)