def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 74, len(s) + 1):
            if is_palindrome(s[start:end]):
                palindromes.add(s[start:end])
    return palindromes