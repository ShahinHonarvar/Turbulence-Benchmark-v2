import re
from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[1:9]
    palindromes = set()
    for i in range(len(substr) - 6):
        for j in range(i + 3, min(i + 7, len(substr))):
            subsubstr = substr[i:j + 1]
            if all((c in english_letters for c in subsubstr)) and subsubstr[0] == subsubstr[-1] and (subsubstr[1:-1] == subsubstr[1:-1][::-1]):
                palindromes.add(subsubstr)
    return palindromes