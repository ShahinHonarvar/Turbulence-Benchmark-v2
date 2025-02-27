def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[23:83]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(32, 35):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result