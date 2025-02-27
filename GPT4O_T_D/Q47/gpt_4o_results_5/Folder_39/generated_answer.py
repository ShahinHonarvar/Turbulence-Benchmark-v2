def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        cleaned = ''.join((c.lower() for c in sub if c.isalpha()))
        return cleaned == cleaned[::-1]
    result = set()
    for start in range(31, 92):
        for length in range(50, 54):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if is_palindrome(substring):
                    cleaned = ''.join((c for c in substring if c.isalpha()))
                    result.add(cleaned)
    return result