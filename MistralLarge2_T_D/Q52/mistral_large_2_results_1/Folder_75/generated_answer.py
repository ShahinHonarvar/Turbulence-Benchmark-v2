def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    length_n = 80
    palindromes = set()
    for i in range(len(s) - length_n + 1):
        substring = s[i:i + length_n]
        if is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes