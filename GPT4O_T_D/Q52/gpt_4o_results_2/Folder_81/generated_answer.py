def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes