def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join([c for c in s if c.isalpha()]).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 149, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes