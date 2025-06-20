def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    min_length = 22
    for start in range(n):
        for end in range(start + min_length, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result