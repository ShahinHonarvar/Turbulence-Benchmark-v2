def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 65):
        sub = s[i:i + 66]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes