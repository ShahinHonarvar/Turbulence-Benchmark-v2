def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letter_only(substring):
        return substring.isalpha()
    palindromes = set()
    s = s.lower()
    n = 36
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_letter_only(substring) and is_palindrome(substring) and (len(substring) >= n):
                palindromes.add(substring)
    return palindromes