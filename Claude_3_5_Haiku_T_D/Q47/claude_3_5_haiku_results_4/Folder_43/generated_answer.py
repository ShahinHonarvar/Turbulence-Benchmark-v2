def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    palindromes = set()
    substring = text[41:90].lower()
    for length in range(23, 39):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes