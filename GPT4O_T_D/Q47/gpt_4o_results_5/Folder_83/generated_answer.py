def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()
    valid_palindromes = set()
    substring = s[75:96]
    for start in range(len(substring)):
        for length in range(7, 10):
            end = start + length
            if end <= len(substring):
                candidate = substring[start:end]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate)
    return valid_palindromes