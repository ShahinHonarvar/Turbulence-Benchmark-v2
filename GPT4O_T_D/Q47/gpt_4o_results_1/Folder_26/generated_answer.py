def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    cleaned_segment = ''.join((c for c in s[24:85] if c.isalpha())).lower()
    n = len(cleaned_segment)
    result = set()
    for length in range(21, 32):
        for i in range(n - length + 1):
            candidate = cleaned_segment[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result