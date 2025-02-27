def palindrome_of_length_n(s, n=97):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes