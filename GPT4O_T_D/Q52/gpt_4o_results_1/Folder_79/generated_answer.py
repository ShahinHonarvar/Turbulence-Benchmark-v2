def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 63):
        substring = s[i:i + 64]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes