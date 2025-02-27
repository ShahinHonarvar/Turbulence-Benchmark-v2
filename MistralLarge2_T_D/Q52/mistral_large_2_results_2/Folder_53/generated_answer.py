def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 68
    length = len(string)
    palindromes = set()
    for i in range(length - n + 1):
        substring = string[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes