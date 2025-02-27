def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substr = s[20:75]
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes