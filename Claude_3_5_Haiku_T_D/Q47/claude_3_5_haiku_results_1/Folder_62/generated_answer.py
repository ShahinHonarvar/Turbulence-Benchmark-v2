def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1] and substr.isalpha()
    palindromes = set()
    substring = s[26:88].lower()
    for start in range(len(substring)):
        for length in range(52, 57):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes