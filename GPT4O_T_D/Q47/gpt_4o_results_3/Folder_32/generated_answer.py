def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        filtered = ''.join(filter(str.isalpha, substring)).lower()
        return filtered == filtered[::-1]
    valid_palindromes = set()
    for length in range(43, 48):
        for start in range(16, 78 - length):
            substring = s[start:start + length]
            if is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes