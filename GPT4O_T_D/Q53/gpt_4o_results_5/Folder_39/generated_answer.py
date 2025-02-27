def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n):
        for j in range(i + 69, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result