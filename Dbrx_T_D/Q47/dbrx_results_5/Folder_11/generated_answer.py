def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    return {s[i:j] for length in range(10, 37) for i in range(24, 98 - length + 1) for j in range(i + length, i + length + 1) if is_palindrome(s[i:j])}