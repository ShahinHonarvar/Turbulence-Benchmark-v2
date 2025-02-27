from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:9] if char.isalpha())).lower()
    palindrome_set = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set