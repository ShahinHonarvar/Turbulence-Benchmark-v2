def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 400):
        substring = s[i:i + 401]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes