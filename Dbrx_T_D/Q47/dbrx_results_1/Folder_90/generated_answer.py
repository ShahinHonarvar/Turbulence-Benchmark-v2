def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    for i in range(106, 281):
        for length in range(136, 152):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes