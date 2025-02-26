def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_alpha_only(substr):
        return substr.isalpha()
    result = set()
    substring = s[103:277]
    for length in range(100, 170):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if is_palindrome(substr) and is_alpha_only(substr):
                result.add(substr)
    return result