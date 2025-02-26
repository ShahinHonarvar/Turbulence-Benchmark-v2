def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1] and substr.isalpha()
    if len(s) <= 88:
        return set()
    substr = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes