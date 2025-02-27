def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    length = len(s)
    for i in range(length):
        for j in range(i + 84, length + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes