def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1] and substr.lower().isalpha()
    if len(s) < 72:
        return set()
    substring = s[32:72]
    valid_palindromes = set()
    for length in range(21, 33):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if is_palindrome(substr):
                valid_palindromes.add(substr)
    return valid_palindromes