def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 71):
        substring = s[i:i + 72]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes