def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1] and substr.isalpha()
    palindromes = set()
    substring = s[29:99].lower()
    for length in range(6, 10):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes