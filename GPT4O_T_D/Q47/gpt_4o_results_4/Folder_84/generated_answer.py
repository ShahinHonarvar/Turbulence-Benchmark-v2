def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[23:78]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    for length in range(13, 41):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                found_palindromes.add(substr)
    return found_palindromes