from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            word = ''.join(sorted([c for c in word if c in eng_letters]))
            counter[word] += 1
    count = sum([c * (c - 1) // 2 for c in counter.values() if c > 1])
    return count <= 464