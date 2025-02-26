def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substring):
        return substring.isalpha() and substring.lower() == substring.lower()[::-1]
    result = set()
    substring = s[21:63]
    for length in range(22, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_letter_palindrome(candidate):
                result.add(candidate)
    return result