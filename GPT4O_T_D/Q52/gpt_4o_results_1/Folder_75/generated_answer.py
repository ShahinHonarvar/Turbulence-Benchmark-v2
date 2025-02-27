def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    result = set()
    for i in range(len(s) - 79):
        substr = s[i:i + 80]
        if is_palindrome(substr):
            result.add(substr)
    return result