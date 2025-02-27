def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s) - 90):
        if is_palindrome(s[i:i + 91]):
            palindromes.add(s[i:i + 91])
    return palindromes