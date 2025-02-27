def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 66):
        substring = s[i:i + 67]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes