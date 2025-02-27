def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 17, n + 1):
            if is_palindrome(s[start:end]):
                result.add(s[start:end])
    return result