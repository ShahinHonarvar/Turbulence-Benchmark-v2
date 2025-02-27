def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        lower_seq = [c.lower() for c in seq if c.isalpha()]
        return lower_seq == lower_seq[::-1]
    n = len(s)
    max_length = min(n, 51)
    result = set()
    for start in range(max_length):
        for length in range(50, 101):
            if start + length <= max_length:
                substring = s[start:start + length]
                if is_palindrome(substring):
                    result.add(''.join([c for c in substring if c.isalpha()]))
    return result