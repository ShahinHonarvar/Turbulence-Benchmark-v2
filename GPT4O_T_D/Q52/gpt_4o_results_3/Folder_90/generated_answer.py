def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = 318
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            result.add(substring)
    return result