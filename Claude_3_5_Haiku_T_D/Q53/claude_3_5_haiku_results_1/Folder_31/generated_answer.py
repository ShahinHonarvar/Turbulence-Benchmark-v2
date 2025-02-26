def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    n = 34
    length = len(string)
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = string[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes