from collections import Counter
from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:8].lower()
    letters = [char for char in string if char.isalpha()]
    palindrome_set = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set