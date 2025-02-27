def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    s = s[12:93]
    s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(s)):
        for length in range(17, 67):
            if start + length <= len(s):
                substring = s[start:start + length]
                if is_palindrome(substring):
                    result.add(substring)
    return result