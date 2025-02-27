def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s)):
        for j in range(i + 30, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                result.add(sub)
    return result