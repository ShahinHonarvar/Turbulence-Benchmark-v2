def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]

    def is_only_letters(s):
        return s.isalpha()
    string = string.lower()
    palindromes = set()
    for length in range(20, len(string) + 1):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes