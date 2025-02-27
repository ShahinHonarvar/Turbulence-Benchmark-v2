def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[30:85]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(12, 21):
            if start + length <= len(s):
                sub = s[start:start + length]
                if is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes