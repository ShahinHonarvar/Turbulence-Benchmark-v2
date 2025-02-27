from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((char for char in string[:6] if char.lower() in letters))
    char_counts = Counter(filtered_string.lower())
    palindromes = set()
    for length in range(5, len(filtered_string) + 1):
        for perm in permutations(char_counts.elements(), length):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
    return palindromes