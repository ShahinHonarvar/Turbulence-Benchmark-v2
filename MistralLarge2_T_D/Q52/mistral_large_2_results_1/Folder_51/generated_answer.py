def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    length = 73
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes