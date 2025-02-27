def palindrome_of_length_at_least_n(s):

    def is_palindrome(text):
        return text == text[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 53, n + 1):
            if is_palindrome(s[start:end]):
                palindromes.add(s[start:end])
    return palindromes