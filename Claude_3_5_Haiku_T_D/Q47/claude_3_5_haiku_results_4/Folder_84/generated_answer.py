def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]

    def is_only_letters(x):
        return x.isalpha()
    result = set()
    for length in range(13, 41):
        for start in range(23, 78 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_only_letters(substring):
                result.add(substring)
    return result