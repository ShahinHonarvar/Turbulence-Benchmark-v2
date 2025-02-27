def palindrome_of_length_n(s):
    n = 47
    palindromes = set()
    length = len(s)

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes