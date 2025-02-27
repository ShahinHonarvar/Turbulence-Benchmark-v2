def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    substr = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes