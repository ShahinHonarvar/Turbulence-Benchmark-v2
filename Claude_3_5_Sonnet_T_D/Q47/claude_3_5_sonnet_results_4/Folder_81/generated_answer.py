def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[12:123]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 221, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result