def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 2, len(s)):
            if is_palindrome(s[start:end + 1]):
                palindromes.add(s[start:end + 1])
    return palindromes