from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    if len(s) < 113:
        return palindromes

    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    for i in range(len(s) - 112):
        for j in range(i, i + 113):
            if is_palindrome(i, j):
                palindromes.add(s[i:j + 1])
    return palindromes