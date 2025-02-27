import re
from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[1:4].lower()
    present_letters = set(substr) & eng_letters
    palindromes = set()
    if len(present_letters) < 2:
        return palindromes
    for i in range(1, len(substr) + 1):
        for j in range(len(substr) - i + 1):
            substr_arrangement = substr[j:j + i]
            if len(substr_arrangement) >= 4 and substr_arrangement == substr_arrangement[::-1] and all((c in present_letters for c in substr_arrangement)):
                palindromes.add(substr_arrangement)
    return palindromes