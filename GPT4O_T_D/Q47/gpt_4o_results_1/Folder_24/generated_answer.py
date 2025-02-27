def palindromes_of_specific_lengths(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    s = s[12:93]
    s = ''.join((c for c in s if c.isalpha())).lower()
    result = set()
    length_range = range(42, 78)
    for pal_length in length_range:
        for i in range(len(s) - pal_length + 1):
            substring = s[i:i + pal_length]
            if is_palindrome(substring):
                result.add(substring)
    return result