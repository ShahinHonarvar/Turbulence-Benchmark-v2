def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    result = set()
    substring = s[18:89]
    for length in range(12, 15):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_letters_only(candidate):
                result.add(candidate)
    return result