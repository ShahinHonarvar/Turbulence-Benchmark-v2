def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes