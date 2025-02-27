def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1] and all((c.isalpha() for c in s))
    result = set()
    s = s.lower()
    for i in range(len(s) - 47):
        for j in range(i + 48, len(s) + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result