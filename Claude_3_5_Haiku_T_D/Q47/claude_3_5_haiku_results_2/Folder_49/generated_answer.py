def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_letter_only(s):
        return s.isalpha()
    result = set()
    for length in range(10, 51):
        for start in range(10, 101 - length + 1):
            substring = text[start:start + length].lower()
            if is_palindrome(substring) and is_letter_only(substring):
                result.add(substring)
    return result