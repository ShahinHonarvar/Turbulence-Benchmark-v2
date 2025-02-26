def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(substring) == 21 and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes