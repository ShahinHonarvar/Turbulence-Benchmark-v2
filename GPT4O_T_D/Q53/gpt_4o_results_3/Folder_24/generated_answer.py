def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = 53
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes