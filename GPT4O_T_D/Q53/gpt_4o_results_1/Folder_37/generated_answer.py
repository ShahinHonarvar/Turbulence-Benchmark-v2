def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 67, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result