def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def is_valid(sub):
        return sub.isalpha()
    n = 87
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n].lower()
        if is_valid(sub) and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes