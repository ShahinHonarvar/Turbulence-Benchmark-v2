def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 69
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            result.add(substring)
    return result