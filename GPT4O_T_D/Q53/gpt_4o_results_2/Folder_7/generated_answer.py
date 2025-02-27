def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = 122
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes