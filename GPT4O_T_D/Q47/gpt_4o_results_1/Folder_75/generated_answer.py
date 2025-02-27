def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[31:75]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(23, 40):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                result.add(substr.lower())
    return result