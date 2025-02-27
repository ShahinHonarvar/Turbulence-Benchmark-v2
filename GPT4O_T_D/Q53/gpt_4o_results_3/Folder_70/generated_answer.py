def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 11, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes