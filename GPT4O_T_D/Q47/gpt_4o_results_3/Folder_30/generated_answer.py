def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    result = set()
    s = s.lower()
    start, end = (14, 90)
    for i in range(start, min(end + 1, len(s))):
        for length in range(55, 72):
            if i + length <= len(s) and i + length <= end + 1:
                substr = ''.join(filter(str.isalpha, s[i:i + length]))
                if len(substr) == length and is_palindrome(substr):
                    result.add(substr)
    return result