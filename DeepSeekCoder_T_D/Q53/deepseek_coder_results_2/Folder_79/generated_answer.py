def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 17, len(s) + 1):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes