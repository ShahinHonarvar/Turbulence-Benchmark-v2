def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 23, n + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result