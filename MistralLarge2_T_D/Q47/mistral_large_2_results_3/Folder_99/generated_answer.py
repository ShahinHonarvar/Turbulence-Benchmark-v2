def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    s = s[127:289].lower()
    palindromes = set()
    for length in range(119, 142):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes