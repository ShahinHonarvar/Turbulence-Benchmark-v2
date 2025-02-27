from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((char for char in string[:6] if char.lower() in letters))
    char_counts = Counter(filtered_string.lower())
    palindromes = set()
    for length in range(4, len(filtered_string) + 1):
        for perm in permutations(filtered_string.lower(), length):
            word = ''.join(perm)
            if word == word[::-1] and all((char_counts[char] >= word.count(char) for char in set(word))):
                palindromes.add(word)
    return palindromes