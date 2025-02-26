def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[12:93]
    for i in range(len(substring)):
        for j in range(i + 42, min(i + 78, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and is_palindrome(substr) and (42 <= len(substr) <= 77):
                result.add(substr)
    return result