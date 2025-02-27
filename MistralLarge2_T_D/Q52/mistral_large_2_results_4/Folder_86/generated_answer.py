def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    length = 181
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes