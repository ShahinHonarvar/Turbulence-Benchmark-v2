def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    n = 83
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes