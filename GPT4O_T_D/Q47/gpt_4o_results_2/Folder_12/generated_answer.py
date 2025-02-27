def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    valid_palindromes = set()
    s = s[62:89]
    s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(s)):
        for length in range(18, 22):
            if start + length <= len(s):
                substr = s[start:start + length]
                if is_palindrome(substr):
                    valid_palindromes.add(substr)
    return valid_palindromes