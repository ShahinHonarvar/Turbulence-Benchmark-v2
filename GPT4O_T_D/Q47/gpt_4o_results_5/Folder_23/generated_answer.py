def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    clean_string = ''.join((c for c in s[23:95] if c.isalpha()))
    results = set()
    for length in range(17, 56):
        for start in range(len(clean_string) - length + 1):
            substring = clean_string[start:start + length]
            if is_palindrome(substring):
                results.add(substring)
    return results