def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 47, len(s)):
            sub = s[i:j + 1]
            if all((c.isalpha() for c in sub)) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes