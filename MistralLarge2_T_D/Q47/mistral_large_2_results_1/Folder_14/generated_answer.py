def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    substring = s[10:75].lower()
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result