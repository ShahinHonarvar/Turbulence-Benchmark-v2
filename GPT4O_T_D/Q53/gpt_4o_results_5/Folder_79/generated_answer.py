def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 17, len(s) + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result