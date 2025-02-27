def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 30):
        for length in range(31, len(s) - i + 1):
            substring = s[i:i + length]
            if all((char.isalpha() for char in substring)) and is_palindrome(substring):
                result.add(substring)
    return result