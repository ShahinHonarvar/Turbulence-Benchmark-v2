def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_only_letters(s):
        return s.isalpha()
    result = set()
    for start in range(155, 284):
        for length in range(104, 121):
            if start + length > len(text):
                break
            substr = text[start:start + length].lower()
            if is_palindrome(substr) and is_only_letters(substr):
                result.add(substr)
    return result