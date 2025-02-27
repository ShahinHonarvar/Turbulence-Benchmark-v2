def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    desired_length = 91
    palindromes = {s[i:i + desired_length] for i in range(len(s) - desired_length + 1) if is_palindrome(s[i:i + desired_length])}
    return palindromes