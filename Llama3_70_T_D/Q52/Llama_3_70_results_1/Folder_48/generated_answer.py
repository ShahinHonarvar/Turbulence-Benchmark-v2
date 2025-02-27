def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 185):
        substr = s[i:i + 186]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes