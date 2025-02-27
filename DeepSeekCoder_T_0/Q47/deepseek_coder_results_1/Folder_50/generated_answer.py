def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(10, 36):
        for i in range(36, 93 - length):
            substring = s[i:i + length].lower()
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result