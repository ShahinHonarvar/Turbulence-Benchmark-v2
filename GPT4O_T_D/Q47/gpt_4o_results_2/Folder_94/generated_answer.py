def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[40:95]
    result = set()
    substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result