def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = len(s)
    palindromes = set()
    for length in range(104, 121):
        for i in range(155, 283 - length + 2):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes