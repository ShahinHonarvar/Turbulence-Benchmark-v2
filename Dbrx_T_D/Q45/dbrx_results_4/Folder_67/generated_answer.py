import re
from collections import defaultdict

def find_palindromes(s):
    english_letters = set()
    for i in range(ord('a'), ord('z') + 1):
        english_letters.add(chr(i))
    palindromes = set()
    for i in range(2, 7):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) >= 5 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes

def palindromes_between_indices(s):
    return find_palindromes(s)