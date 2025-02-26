def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    string = string.lower()
    palindromes = set()
    for length in range(30, len(string) + 1):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes