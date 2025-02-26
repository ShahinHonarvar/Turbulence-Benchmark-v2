def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    result = set()
    for length in range(136, 161):
        for start in range(100, 296 - length + 1):
            substring = text[start:start + length].lower()
            if is_palindrome(substring):
                result.add(substring)
    return result