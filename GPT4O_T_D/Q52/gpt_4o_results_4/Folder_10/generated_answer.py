def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - 53):
        substr = s[i:i + 54]
        if is_palindrome(substr):
            result.add(substr)
    return result