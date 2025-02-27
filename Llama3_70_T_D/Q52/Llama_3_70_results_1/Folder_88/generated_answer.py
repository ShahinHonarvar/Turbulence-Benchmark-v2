def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for i in range(len(s) - 12):
        sub = s[i:i + 13]
        if sub.isalpha() and is_palindrome(sub):
            result.add(sub)
    return result