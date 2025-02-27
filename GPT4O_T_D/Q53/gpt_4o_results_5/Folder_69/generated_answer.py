def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = 98

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(s)
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes