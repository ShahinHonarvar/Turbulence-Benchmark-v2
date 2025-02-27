from collections import Counter
  import math

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(1, 6) if string[i].isalpha()]
    if len(letters) < 6:
        return set()
    letter_counts = Counter(letters)
    odd_counts = [c for c in letter_counts.values() if c % 2 == 1]
    if len(odd_counts) > 1:
        return set()
    permutations = math.factorial(len(letters))
    for count in letter_counts.values():
        permutations //= math.factorial(count)
    return set([''.join(letters)[:i] + ''.join(reversed(letters))[0:len(letters) - i] for i in range(len(letters))] * permutations)