def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    palindromes = set()
    for i in range(50, len(s) - 50 + 1):
        for length in range(50, 101):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes