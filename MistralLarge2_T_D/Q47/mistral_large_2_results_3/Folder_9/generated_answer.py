def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substr = s[:301]
    palindromes = set()
    for length in range(50, 61):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes