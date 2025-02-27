def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s[32:72])).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(21, 33):
            if start + length <= len(s):
                substring = s[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes