def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    return {s[1:9].lower() for s in set(s[1:9]) if is_palindrome(s[1:9]) and len(s[1:9]) >= 4}