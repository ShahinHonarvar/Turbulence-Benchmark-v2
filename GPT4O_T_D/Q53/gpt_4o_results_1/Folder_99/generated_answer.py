def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join([char.lower() for char in s if char.isalpha()])
    n = 115
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes