def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]

    def is_only_letters(x):
        return x.isalpha()
    palindromes = set()
    for length in range(45, 53):
        for start in range(11, 97 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring.lower())
    return palindromes