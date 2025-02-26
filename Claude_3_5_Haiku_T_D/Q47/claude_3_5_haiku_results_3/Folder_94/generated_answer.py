def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]

    def is_only_letters(x):
        return x.isalpha()
    palindromes = set()
    s = s.lower()
    for length in range(45, 52):
        for start in range(40, 95 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes