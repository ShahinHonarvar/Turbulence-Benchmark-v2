def palindromes_of_specific_lengths(s):
    substr = s[40:95]
    valid_chars = [c for c in substr if c.isalpha()]
    lower_valid_chars = ''.join(valid_chars).lower()

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    for length in range(45, 52):
        if length <= len(lower_valid_chars):
            for start in range(len(lower_valid_chars) - length + 1):
                candidate = lower_valid_chars[start:start + length]
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes