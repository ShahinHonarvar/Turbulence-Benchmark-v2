def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substr = s[11:98].lower()
    palindromes = set()
    for length in range(29, 63):
        for start in range(len(substr) - length + 1):
            substring = substr[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes