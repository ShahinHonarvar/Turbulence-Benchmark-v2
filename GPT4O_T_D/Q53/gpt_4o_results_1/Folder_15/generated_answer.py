def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for start in range(n):
        for end in range(start + 3, n):
            substring = s[start:end + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes