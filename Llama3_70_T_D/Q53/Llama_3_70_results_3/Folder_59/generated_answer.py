def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, len(s) + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes