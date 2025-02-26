def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[40:95]
    for i in range(len(substring)):
        for j in range(i + 45, min(i + 52, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result