def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    result = set()
    substring = s[41:90]
    for length in range(23, 39):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result