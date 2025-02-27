from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    filtered_string = ''.join((char for char in string[2:7] if char.isalpha()))
    char_counts = Counter(filtered_string.lower())
    palindromes = set()
    for length in range(5, len(filtered_string) + 1):
        for perm in permutations(char_counts.elements(), length):
            word = ''.join(perm)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes