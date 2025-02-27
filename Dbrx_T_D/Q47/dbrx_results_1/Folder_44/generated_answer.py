def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    for i in range(18, 99):
        for length in range(31, 52):
            substring = s[i:i + length]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes