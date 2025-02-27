def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 42
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes