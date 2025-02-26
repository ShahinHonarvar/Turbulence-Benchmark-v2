def palindromes_of_specific_lengths(s):

    def is_palindrome(text):
        return text == text[::-1]
    result = set()
    substring = s[15:90]
    substring = ''.join((c for c in substring if c.isalpha()))
    substring = substring.lower()
    for length in range(40, 73):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result