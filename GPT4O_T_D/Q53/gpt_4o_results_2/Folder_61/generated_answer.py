def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)

    def is_palindrome(start, end):
        return s[start:end + 1] == s[start:end + 1][::-1]
    for start in range(n):
        for end in range(start + 4, n):
            if is_palindrome(start, end):
                result.add(s[start:end + 1])
    return result