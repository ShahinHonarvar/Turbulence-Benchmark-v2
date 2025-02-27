import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    min_length = 138
    n = len(s)
    result = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for i in range(n):
        for j in range(i + min_length, n + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result