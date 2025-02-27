def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    min_length = 27
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + min_length, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes