from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[0:7].lower())
    keys = ''.join(letters.keys())
    palindrome_set = set()
    for i in range(6, len(keys) + 1):
        for j in permutations(keys, i):
            word = ''.join(j)
            if word == word[::-1] and word not in palindrome_set:
                palindrome_set.add(word)
    return palindrome_set