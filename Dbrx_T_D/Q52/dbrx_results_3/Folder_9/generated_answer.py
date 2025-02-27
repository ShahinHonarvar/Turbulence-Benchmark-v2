import re
from collections import defaultdict

def palindrome_of_length_n(s):
    n = 72
    s = s.lower()
    letters = set(s)
    palindromes = set()
    for letter in letters:
        if s.count(letter) >= n:
            palindromes.add(letter * n)
            break
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        frequency = defaultdict(int)
        for j in range(len(substring)):
            frequency[substring[j:j + 1]] += 1
        if all((count % 2 == 0 or count == 1 for count in frequency.values())):
            palindromes.add(substring)
    return palindromes