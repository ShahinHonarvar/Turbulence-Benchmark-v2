import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(6, 10):
        if i < len(s):
            letters[s[i].lower()] += 1
    palindromes = set()
    for char in letters:
        if letters[char] >= 2:
            palindromes.add(char * 2)
        if letters[char] >= 4:
            palindromes.add(char * 4)
        for other in letters:
            if char != other and letters[other] >= 1:
                palindromes.add(char + other + char)
                palindromes.add(other + char + other)
    return palindromes