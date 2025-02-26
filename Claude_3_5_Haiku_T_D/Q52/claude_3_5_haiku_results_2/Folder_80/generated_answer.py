def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]

    def is_only_letters(s):
        return all((c.isalpha() for c in s))
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 275):
        substring = string[i:i + 276]
        if len(substring) == 276 and is_palindrome(substring) and is_only_letters(substring):
            palindromes.add(substring)
    return palindromes