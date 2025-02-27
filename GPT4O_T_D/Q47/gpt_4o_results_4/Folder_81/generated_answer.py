def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for start in range(0, len(s) - 11):
        for length in range(12, min(221, len(s) - start + 1)):
            if start >= 12 and start + length - 1 <= 122:
                substring = s[start:start + length]
                if is_palindrome(substring):
                    result.add(substring)
    return result