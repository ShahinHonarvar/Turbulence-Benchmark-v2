from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((char for char in string[:7] if char.lower() in letters))
    letter_counts = Counter(filtered_string.lower())
    palindromes = set()
    for i in range(5, len(filtered_string) + 1):
        for permutation in permutations(filtered_string.lower(), i):
            word = ''.join(permutation)
            if word == word[::-1] and all((letter_counts[char] >= Counter(word)[char] for char in word)):
                palindromes.add(word)
    return palindromes