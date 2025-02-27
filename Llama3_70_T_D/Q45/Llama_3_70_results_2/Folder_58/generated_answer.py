from itertools import permutations
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:7])
    letters = [letter.lower() for letter in letters]
    letters_set = set(letters)
    palindromes = set()
    for letters_combination in permutations(letters_set, 6):
        palindrome = ''.join(letters_combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes

def palindromes_between_indices1(s):
    letters = re.findall('[a-zA-Z]', s[:7].lower())
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(start, end, current):
        if len(current) >= 6 and is_palindrome(current):
            palindromes.add(current)
        for i in range(start, end):
            backtrack(i + 1, end, current + letters[i])
    backtrack(0, len(letters), '')
    return palindromes