def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1] and s.isalpha()
    valid_palindromes = set()
    for length in range(45, 53):
        for start in range(11, 97 - length + 1):
            substring = text[start:start + length]
            if is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes