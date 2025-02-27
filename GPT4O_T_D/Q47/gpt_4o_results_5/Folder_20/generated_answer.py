def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s[20:75].lower()))
    n = len(s)
    for length in range(36, 43):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result