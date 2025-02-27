def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    result = set()
    for start in range(len(s)):
        for end in range(start + 49, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result