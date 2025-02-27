def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring[::-1].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    start = 29
    end = 96
    if start < len(s) and end < len(s):
        for i in range(start, end + 1):
            for length in range(12, 19):
                if i + length <= end + 1:
                    substring = s[i:i + length]
                    if is_palindrome(substring):
                        palindromes.add(substring)
    return palindromes