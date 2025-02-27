from collections import Counter
	from itertools import permutations

def if_contains_anagrams(lst):
    cnt = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            for p in permutations(word):
                p = ''.join(p)
                if p != word and p in lst:
                    cnt += 1
                    break
    return cnt <= 72