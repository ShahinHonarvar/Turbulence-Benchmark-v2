from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = ''.join([ch for ch in s[2:7] if ch.isalpha()])
    unique_palindromes = set()
    for r in range(5, len(sub_string) + 1):
        for p in permutations(sub_string, r):
            word = ''.join(p)
            if is_palindrome(word):
                unique_palindromes.add(word)
    return unique_palindromes