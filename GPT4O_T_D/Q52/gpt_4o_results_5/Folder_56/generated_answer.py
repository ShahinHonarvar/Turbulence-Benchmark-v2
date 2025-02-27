def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if is_palindrome(substring):
            result.add(substring)
    return result