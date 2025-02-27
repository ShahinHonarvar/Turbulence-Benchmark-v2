def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = ''.join([c for c in s[17:73] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes