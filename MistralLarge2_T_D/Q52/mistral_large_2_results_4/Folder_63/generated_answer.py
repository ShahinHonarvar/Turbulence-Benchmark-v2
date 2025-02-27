def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    n = 18
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and is_palindrome(substring.lower()):
            result.add(substring)
    return result