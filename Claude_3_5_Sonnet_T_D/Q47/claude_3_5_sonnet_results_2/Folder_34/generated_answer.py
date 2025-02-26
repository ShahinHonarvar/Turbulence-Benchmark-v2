def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substr = s[200:301]
    for i in range(len(substr)):
        for j in range(i + 10, min(i + 51, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result