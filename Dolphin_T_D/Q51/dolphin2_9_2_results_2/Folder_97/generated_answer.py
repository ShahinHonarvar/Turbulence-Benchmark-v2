from collections import Counter
	from itertools import permutations

def if_contains_anagrams(lst):
    c = 0
    for el in lst:
        if len(el) >= 3 and set(el.lower()) <= set('qwertyuiopasdfghjklzxcvbnm'):
            c += sum((all((v == Counter(permut.lower())[k] for k, v in Counter(el.lower()).items())) for permut in permutations(el.lower()) if permut != el.lower()))
    return c // 2 <= 18