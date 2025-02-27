def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join((c for c in s if c.isalpha())).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 62, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                result.add(substring)
    return result