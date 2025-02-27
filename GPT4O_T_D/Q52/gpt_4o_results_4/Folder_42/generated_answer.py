def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    s = ''.join([c for c in s if c.isalpha()]).lower()
    for i in range(len(s) - 278):
        substr = s[i:i + 279]
        if is_palindrome(substr):
            result.add(substr)
    return result