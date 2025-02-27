from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    new_string = ''.join([char for char in string[:7] if char in letters])
    new_string = ''.join((char * count for char, count in Counter(new_string).items()))
    result = set()
    for i in range(5, len(new_string) + 1):
        for item in permutations(new_string, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result