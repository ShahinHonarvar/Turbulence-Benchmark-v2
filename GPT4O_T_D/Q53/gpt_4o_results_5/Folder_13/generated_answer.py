def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    lower_s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    n = len(lower_s)
    for i in range(n):
        for j in range(i + 52, n + 1):
            if is_palindrome(lower_s[i:j]):
                palindromes.add(lower_s[i:j])
    return palindromes