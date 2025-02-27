from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(5, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if len(substring) >= 6 and set(substring) <= english_letters:
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]