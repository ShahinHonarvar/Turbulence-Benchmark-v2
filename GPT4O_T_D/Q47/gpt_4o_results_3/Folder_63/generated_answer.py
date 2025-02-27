def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    filtered = ''.join([c.lower() for c in s[33:86] if c.isalpha()])
    result = set()
    for length in range(26, 32):
        for i in range(len(filtered) - length + 1):
            substring = filtered[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result