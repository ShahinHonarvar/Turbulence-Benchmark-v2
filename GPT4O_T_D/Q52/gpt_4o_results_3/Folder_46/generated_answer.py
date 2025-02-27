def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 464
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            result.add(substring)
    return result