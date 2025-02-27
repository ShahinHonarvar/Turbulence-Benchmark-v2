def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    for start in range(len(s)):
        for end in range(start + 80, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes