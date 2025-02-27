def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for start in range(n - 41):
        for end in range(start + 42, n + 1):
            if is_palindrome(s[start:end]):
                palindromes.add(s[start:end])
    return palindromes