def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    normalized_str = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    for i in range(len(normalized_str)):
        for j in range(i + 57, len(normalized_str) + 1):
            substring = normalized_str[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result