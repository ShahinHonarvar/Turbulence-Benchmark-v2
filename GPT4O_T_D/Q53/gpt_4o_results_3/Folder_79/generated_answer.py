def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 17
    res = set()
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + n, length + 1):
            if is_palindrome(s[i:j]):
                res.add(s[i:j])
    return res