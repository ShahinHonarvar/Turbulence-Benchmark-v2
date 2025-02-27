def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[35:89]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                result.add(substr)
    return result