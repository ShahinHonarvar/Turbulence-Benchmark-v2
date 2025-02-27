def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1] and substring.isalpha()
    palindromes = set()
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes