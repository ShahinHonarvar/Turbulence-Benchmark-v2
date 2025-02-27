def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[43:96].lower()
    valid_palindromes = set()
    for start in range(len(s)):
        for length in range(18, 48):
            if start + length <= len(s):
                substring = ''.join(filter(str.isalpha, s[start:start + length]))
                if len(substring) == length and is_palindrome(substring):
                    valid_palindromes.add(substring)
    return valid_palindromes