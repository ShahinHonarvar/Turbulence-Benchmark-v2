def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substr):
        return substr.isalpha() and substr.lower() == substr.lower()[::-1]
    if len(s) < 301:
        return set()
    substr = s[100:301]
    result = set()
    for length in range(50, 101):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if is_letter_palindrome(candidate):
                result.add(candidate.lower())
    return result