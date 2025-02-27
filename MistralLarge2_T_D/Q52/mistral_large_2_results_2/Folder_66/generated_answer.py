def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 25
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes