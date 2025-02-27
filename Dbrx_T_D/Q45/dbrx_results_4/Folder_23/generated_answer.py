from collections import defaultdict
import re

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindrome_set = set()
    if len(s) < 7:
        return palindrome_set
    s = s.lower()
    for i in range(7, len(s) - 6):
        substring = s[i - 7:i + 1]
        letters = set(substring)
        if letters.issubset(english_letters):
            palindrome_substring = [x for x in substring if x in letters]
            palindrome_substring = ''.join(palindrome_substring)
            palindromes = create_palindromes(palindrome_substring)
            palindrome_set.update(palindromes)
    return palindrome_set

def create_palindromes(s):
    palindromes = set()
    if len(s) == 4:
        palindromes.add(s)
    else:
        for i in range(len(s) - 3):
            palindromes.add(s[i:i + 4])
            palindromes.add(s[i:i + 4][::-1])
    return palindromes