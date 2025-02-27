def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i + 21, len(s) + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes