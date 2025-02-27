def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[12:93]
    result = set()
    for i in range(len(s)):
        for j in range(17, 67):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.isalpha() and is_palindrome(substring.lower()):
                    result.add(substring)
    return result