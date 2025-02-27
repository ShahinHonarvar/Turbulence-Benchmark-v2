def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substr = s[12:93].lower()
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes