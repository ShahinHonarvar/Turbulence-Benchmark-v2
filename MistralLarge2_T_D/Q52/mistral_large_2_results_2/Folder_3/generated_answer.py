def palindrome_of_length_n(s, n=100):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes