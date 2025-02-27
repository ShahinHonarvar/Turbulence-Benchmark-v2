from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    potential_palindromes = set()
    for i in range(5):
        for j in range(i, i + 5):
            sub_s = s[j]
            if sub_s.lower() in english_letters:
                potential_palindromes.add(sub_s.lower())
    palindromes = set()
    for length in range(5, 0, -1):
        for palindrome in potential_palindromes:
            if len(palindrome) == length and is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]