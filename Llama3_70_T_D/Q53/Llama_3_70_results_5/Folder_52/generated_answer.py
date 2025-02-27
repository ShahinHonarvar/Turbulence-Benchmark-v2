def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 14, len(s) + 1):
            sub = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(sub):
                result.add(sub)
    return result