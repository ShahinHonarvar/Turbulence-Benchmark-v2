from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    counter = Counter()
    result = []
    for i in range(len(lst)):
        s = ''.join(sorted(lst[i].lower()))
        if len(s) >= 3:
            counter[s] += 1
    for key in counter:
        perm = [''.join(p) for p in permutations(key)]
        for i in perm:
            if i != key:
                result.append(i)
    final_counter = Counter(result)
    flag = 0
    for value in final_counter.values():
        if value > 36:
            flag = 1
    if flag:
        return False
    else:
        return True