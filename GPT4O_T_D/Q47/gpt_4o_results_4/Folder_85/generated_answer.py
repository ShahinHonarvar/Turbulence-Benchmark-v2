def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[29:99]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for start in range(len(s)):
        for length in range(6, 10):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if is_palindrome(substring):
                    result.add(substring)
    return result