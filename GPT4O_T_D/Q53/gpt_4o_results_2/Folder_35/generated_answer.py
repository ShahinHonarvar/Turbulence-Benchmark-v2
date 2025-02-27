def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 26
    palindromes = set()
    length = len(s)

    def is_palindrome(subs):
        return subs == subs[::-1]
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes