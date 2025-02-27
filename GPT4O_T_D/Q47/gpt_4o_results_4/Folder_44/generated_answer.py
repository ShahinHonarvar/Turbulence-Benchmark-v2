def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = ''.join(filter(str.isalpha, s[18:99])).lower()
    palindromes = set()
    n = len(s)
    for start in range(n):
        for length in range(31, 52):
            end = start + length
            if end <= n:
                substr = s[start:end]
                if is_palindrome(substr):
                    palindromes.add(substr)
    return palindromes