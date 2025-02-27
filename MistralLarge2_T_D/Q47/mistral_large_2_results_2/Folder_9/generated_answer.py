def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(50, 61):
        for i in range(301 - length):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result