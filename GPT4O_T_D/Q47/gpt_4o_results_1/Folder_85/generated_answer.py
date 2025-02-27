def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    res = set()
    substring = s[29:99].lower()
    for start in range(len(substring)):
        for length in range(6, 10):
            if start + length <= len(substring):
                sub = substring[start:start + length]
                if sub.isalpha() and is_palindrome(sub):
                    res.add(s[29 + start:29 + start + length])
    return res