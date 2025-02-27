from itertools import combinations
from collections import defaultdict

def palindrome_of_length_n(string):
    palindromes = set()
    for start, end in combinations(range(len(string) - 106 + 1), 2):
        substring = string[start:end + 1]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes if palindromes else set()