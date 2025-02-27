def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    set_palindromes = set()
    filtered_s = ''.join((c for c in s[17:96] if c.isalpha()))
    n = len(filtered_s)
    for length in range(13, 50):
        for start in range(n - length + 1):
            substring = filtered_s[start:start + length]
            if is_palindrome(substring):
                set_palindromes.add(substring)
    return set_palindromes