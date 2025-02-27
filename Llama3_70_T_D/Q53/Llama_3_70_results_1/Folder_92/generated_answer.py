def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(10, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes