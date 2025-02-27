def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[32:80]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result