def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = 85
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes