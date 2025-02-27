from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    chars = [string[i] for i in range(7) if string[i] in letters]
    char_counts = Counter(chars)
    palindrome_set = set()
    for perm in permutations(char_counts.elements()):
        word = ''.join(perm)
        if len(word) < 6:
            continue
        if word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set