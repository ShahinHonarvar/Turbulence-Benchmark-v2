from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    c = Counter
    for word in lst:
        if len(word) >= 3:
            word_permutations = [''.join(p) for p in permutations(word.lower())]
            for perm in word_permutations[1:]:
                if perm in lst and perm != word:
                    count += 1
                    lst.remove(perm)
                    break
    return count <= 57