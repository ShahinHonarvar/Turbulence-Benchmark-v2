def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(54, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes