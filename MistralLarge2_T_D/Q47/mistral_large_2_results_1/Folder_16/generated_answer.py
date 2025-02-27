def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[15:87].lower()
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes