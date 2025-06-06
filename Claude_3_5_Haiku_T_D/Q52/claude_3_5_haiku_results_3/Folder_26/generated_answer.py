def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 365):
        substring = string[i:i + 366]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes