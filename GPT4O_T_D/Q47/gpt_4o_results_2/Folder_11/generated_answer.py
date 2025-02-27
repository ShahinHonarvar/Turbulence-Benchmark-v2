def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    lowercase_s = ''.join(filter(str.isalpha, s[24:98].lower()))
    result = set()
    n = len(lowercase_s)
    for length in range(10, 37):
        for start in range(n - length + 1):
            substr = lowercase_s[start:start + length]
            if is_palindrome(substr):
                original_substr = s[start + 24:start + 24 + length]
                result.add(original_substr)
    return result