def palindrome_of_length_at_least_n(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 137, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes