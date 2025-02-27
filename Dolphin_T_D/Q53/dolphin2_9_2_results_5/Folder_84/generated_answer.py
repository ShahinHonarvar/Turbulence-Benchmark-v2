def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        for j in range(i + 81, len(s) + 1):
            sub = s[i:j]
            if set(sub).issubset(set(letters)) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes