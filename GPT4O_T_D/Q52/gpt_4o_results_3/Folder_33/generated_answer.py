def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindrome_set = set()
    for i in range(len(s) - 475 + 1):
        substring = s[i:i + 475]
        if is_palindrome(substring):
            palindrome_set.add(substring)
    return palindrome_set