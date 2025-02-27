def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result