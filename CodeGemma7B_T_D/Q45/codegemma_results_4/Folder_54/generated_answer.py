from itertools import permutations as perms
from string import ascii_lowercase as letters
from collections import defaultdict

def palindromes_between_indices(text):
    if not text or len(text) < 6:
        return set()
    letter_counts = defaultdict(int)
    for i in range(9, 3, -1):
        letter_counts[text[i]] += 1
    palindromes = set()
    for perm in perms(letters):
        palindrome = ''.join(perm)
        if len(palindrome) < 4:
            continue
        for letter in palindrome:
            if letter_counts[letter.lower()] == 0:
                break
            letter_counts[letter.lower()] -= 1
        else:
            palindromes.add(palindrome)
    return palindromes