from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word not in c:
                c[sorted_word] = 1
            else:
                c[sorted_word] += 1
    count = 0
    for v in c.values():
        if v >= 2:
            count += v * (v - 1) // 2
    return count >= 30