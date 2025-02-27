from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            for perm in permutations(word):
                if ''.join(perm) in lst and ''.join(perm) != word:
                    count += 1
                    if count >= 475:
                        return True
    return count >= 475