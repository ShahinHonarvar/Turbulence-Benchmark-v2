def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for start in range(n):
        for end in range(start + 70, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result