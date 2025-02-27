def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join([c.lower() for c in s[1:300] if c.isalpha()])
    palindromes = set()
    for start in range(len(s)):
        for length in range(3, 11):
            if start + length <= len(s):
                substring = s[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes