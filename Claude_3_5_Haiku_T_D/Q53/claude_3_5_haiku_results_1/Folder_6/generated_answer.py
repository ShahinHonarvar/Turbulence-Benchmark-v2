def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    palindromes = set()
    s = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 22, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes