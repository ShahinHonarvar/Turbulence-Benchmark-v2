def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    valid_chars = ''.join((c for c in s if c.isalpha()))
    substring = valid_chars[16:95]
    palindromes = set()
    for length in range(39, 53):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return set(palindromes)