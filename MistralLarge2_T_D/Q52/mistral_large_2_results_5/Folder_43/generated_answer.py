def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = 51
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes