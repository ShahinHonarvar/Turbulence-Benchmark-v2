def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    string = string[12:93].lower()
    palindromes = set()
    for length in range(42, 78):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes