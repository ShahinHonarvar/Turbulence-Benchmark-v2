def palindromes_of_specific_lengths(s):
    s_sub = s[29:97].lower()
    alphabet_only_sub = ''.join(filter(str.isalpha, s_sub))
    result = set()

    def is_palindrome(seq):
        return seq == seq[::-1]
    for length in range(12, 19):
        for start in range(len(alphabet_only_sub) - length + 1):
            substring = alphabet_only_sub[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result