def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    for length in range(3, 11):
        for i in range(1, 300 - length + 2):
            substr = s[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr.lower())
    return palindromes