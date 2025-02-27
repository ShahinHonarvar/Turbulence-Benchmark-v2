def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 63, length + 1):
            substr = s[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes