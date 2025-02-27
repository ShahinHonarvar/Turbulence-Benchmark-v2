def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    n = min(101, len(s))
    for i in range(n):
        for j in range(i + 3, min(i + 16, n + 1)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub) and (3 <= len(sub) <= 15):
                palindromes.add(sub.lower())
    return palindromes