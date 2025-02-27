def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s_filtered = ''.join(filter(str.isalpha, s[43:96])).lower()
    length_range = range(18, 48)
    palindromes = set()
    for start in range(len(s_filtered)):
        for length in length_range:
            end = start + length
            if end <= len(s_filtered):
                substring = s_filtered[start:end]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes