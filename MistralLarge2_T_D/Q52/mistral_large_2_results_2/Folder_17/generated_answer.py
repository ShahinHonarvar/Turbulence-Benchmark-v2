def palindrome_of_length_n(s: str):

    def is_palindrome(sub: str) -> bool:
        return sub.lower() == sub.lower()[::-1]
    n = 289
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub.lower())
    return palindromes