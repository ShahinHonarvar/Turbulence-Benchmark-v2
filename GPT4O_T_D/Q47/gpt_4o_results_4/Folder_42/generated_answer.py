def palindromes_of_specific_lengths(s):

    def is_palindrome(check_str):
        return check_str == check_str[::-1]
    s = ''.join((c for c in s if c.isalpha())).lower()
    s = s[43:96]
    palindrome_set = set()
    for length in range(18, 48):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindrome_set.add(substring)
    return palindrome_set