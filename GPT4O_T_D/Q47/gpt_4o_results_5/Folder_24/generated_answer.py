def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    filtered_str = ''.join((c for c in s[12:93] if c.isalpha())).lower()
    palindromes = set()
    for length in range(42, 78):
        for start in range(len(filtered_str) - length + 1):
            substr = filtered_str[start:start + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes