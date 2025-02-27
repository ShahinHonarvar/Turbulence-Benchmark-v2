def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindrome_set = set()
    for i in range(n - 22):
        substr = s[i:i + 23]
        if is_palindrome(substr):
            palindrome_set.add(substr)
    return palindrome_set