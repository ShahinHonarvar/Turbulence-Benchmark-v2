def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for size in range(70, len(s) + 1):
        for i in range(len(s) - size + 1):
            substring = s[i:i + size]
            if is_palindrome(substring):
                result.add(substring)
    return result