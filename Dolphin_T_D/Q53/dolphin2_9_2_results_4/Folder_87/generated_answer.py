def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    length = 18
    palindromes = set()
    while length <= len(s):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
        length += 1
    return palindromes