def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substring = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            filtered_substr = ''.join(filter(str.isalpha, substr)).lower()
            if len(filtered_substr) == length and is_palindrome(filtered_substr):
                palindromes.add(filtered_substr)
    return palindromes