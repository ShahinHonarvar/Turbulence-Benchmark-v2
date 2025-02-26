def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(substring) == 40 and is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes