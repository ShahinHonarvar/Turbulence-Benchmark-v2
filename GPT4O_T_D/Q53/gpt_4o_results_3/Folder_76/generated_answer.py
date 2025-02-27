def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join([c for c in s if c.isalpha()]).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 137, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes