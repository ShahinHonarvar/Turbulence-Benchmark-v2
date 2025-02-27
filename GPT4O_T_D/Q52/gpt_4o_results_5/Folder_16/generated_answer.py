def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = 255
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring):
            result.add(substring)
    return result