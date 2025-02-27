def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()
    s = ''.join(filter(str.isalpha, s[15:90]))
    pals = set()
    for length in range(40, 73):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                pals.add(substring)
    return pals