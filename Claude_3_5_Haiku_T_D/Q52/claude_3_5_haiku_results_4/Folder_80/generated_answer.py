def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    for i in range(len(s) - 275):
        substring = s[i:i + 276]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes