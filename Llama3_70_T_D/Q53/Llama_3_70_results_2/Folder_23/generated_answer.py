def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 19, len(s) + 1):
            sub = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes