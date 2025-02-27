def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    n = 149
    lower_s = ''.join(filter(str.isalpha, s)).lower()
    length = len(lower_s)
    palindromes = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = lower_s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes