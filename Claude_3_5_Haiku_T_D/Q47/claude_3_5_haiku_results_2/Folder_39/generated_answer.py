def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_letter_only(substr):
        return substr.isalpha()
    result = set()
    substring = s[31:92].lower()
    for length in range(50, 54):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letter_only(candidate):
                result.add(candidate)
    return result