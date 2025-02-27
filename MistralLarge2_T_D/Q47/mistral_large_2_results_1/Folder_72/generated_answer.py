def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[26:91].lower()
    palindromes = set()
    for length in range(27, 59):
        for start in range(26, 91 - length + 1):
            sub = substring[start - 26:start - 26 + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes