from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    cnt = Counter()
    n = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            for p in permutations(word):
                ana = ''.join(p)
                if ana in cnt and cnt[ana] == 1:
                    n += 1
                else:
                    cnt[ana] = 1
    if n >= 52:
        return True
    else:
        return False