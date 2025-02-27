from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (2, 8)
    letters = defaultdict(int)
    for i in range(start, end + 1):
        if s[i].isalpha():
            letters[s[i].lower()] += 1
    palindromes = {x for x in letters if is_palindrome(x)}
    return palindromes