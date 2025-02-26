def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[11:94]
    for i in range(len(substring)):
        for j in range(i + 34, min(i + 55, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate) and (34 <= len(candidate) <= 54):
                result.add(candidate)
    return result