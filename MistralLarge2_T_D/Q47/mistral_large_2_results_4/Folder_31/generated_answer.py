def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    result = set()
    s = s[11:84].lower()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result