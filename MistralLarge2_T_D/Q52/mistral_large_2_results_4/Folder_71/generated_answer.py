def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    length = 78
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes