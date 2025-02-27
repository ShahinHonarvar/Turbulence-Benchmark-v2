from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((c for c in string[:6] if c.lower() in letters))
    char_counts = Counter(filtered_string.lower())
    palindromes = set()
    for i in range(4, len(filtered_string) + 1):
        for p in permutations(filtered_string.lower(), i):
            word = ''.join(p)
            if word == word[::-1] and Counter(word) <= char_counts:
                palindromes.add(word)
    return palindromes