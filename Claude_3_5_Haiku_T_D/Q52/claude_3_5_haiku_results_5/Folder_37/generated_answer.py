def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes