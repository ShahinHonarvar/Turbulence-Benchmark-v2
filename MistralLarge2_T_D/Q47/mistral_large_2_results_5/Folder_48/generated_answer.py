def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    for length in range(104, 121):
        for i in range(155, 283 - length + 2):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes