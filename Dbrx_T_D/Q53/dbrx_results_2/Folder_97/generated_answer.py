from collections import defaultdict

def is_english_letter(c):
    return c.isalpha()

def to_lower(c):
    return c.lower()

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (to_lower(s[left]) == to_lower(s[right])):
        left -= 1
        right += 1
    return s[left + 1:right]

def find_palindromes(s):
    s = ''.join(filter(is_english_letter, s))
    palindromes = set()
    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i + 1)
        if len(odd_palindrome) >= 138:
            palindromes.add(odd_palindrome)
        if len(even_palindrome) >= 138:
            palindromes.add(even_palindrome)
    return palindromes

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s) if any((is_english_letter(c) for c in s)) else set()