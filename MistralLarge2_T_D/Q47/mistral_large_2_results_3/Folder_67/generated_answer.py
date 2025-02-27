def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    substring = s[65:100].lower()
    for length in range(26, 34):
        for i in range(100 - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes