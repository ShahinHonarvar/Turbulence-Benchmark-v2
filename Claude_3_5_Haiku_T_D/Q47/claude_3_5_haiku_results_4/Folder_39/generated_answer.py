def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substr):
        return substr.isalpha() and substr == substr[::-1]
    result = set()
    substring = s[31:92]
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_letter_palindrome(candidate):
                result.add(candidate)
    return result