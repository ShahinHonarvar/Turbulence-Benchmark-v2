def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(64, len(s) + 1):
        for i in range(len(s) - length + 1):
            if is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes