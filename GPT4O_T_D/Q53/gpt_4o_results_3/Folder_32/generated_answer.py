def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for start in range(n):
        for end in range(start + 70, n + 1):
            if is_palindrome(s[start:end]):
                result.add(s[start:end])
    return result