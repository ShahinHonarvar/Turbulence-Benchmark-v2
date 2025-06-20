def palindrome_of_length_at_least_n(s):

    def is_palindrome(st):
        return st == st[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 43
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes