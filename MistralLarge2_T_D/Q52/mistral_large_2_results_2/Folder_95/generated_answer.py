def palindrome_of_length_n(s):
    n = 87
    palindromes = set()

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes