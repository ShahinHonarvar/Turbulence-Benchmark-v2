def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    n = 84
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n].lower()
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes