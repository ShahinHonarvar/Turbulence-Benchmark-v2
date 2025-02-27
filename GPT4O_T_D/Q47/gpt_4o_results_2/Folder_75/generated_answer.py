def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s[31:75]))
    for length in range(23, 40):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                result.add(substr)
    return result