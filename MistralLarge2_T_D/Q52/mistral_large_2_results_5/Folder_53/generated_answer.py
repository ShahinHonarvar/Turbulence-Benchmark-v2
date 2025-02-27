def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 68
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring.lower()) and substring.isalpha():
            palindromes.add(substring)
    return palindromes