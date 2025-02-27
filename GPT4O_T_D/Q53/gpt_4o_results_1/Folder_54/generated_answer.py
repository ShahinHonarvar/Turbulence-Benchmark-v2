def palindrome_of_length_at_least_n(s):

    def is_palindrome(check_str):
        return check_str == check_str[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 74, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result