def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    n = 95
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes