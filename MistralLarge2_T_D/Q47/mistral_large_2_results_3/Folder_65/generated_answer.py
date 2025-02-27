def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[15:96]
    palindromes = set()
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes