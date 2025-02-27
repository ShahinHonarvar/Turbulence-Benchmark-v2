def palindrome_of_length_at_least_n(s):

    def is_palindrome(st):
        return st == st[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 83, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes