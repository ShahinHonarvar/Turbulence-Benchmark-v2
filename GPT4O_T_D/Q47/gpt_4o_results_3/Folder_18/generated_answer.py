def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[11:84].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(13, 67):
            if start + length <= len(s):
                substring = s[start:start + length]
                if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes