from collections import Counter
import functools

def if_contains_anagrams(lst):
    n = len(lst)
    anagrams = [0] * n
    for i in range(n):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, n):
            if len(lst[j]) < 3:
                continue
            if functools.cmp_to_key(lambda x, y: 0 if x == y else 1)(Counter(lst[i].lower()), Counter(lst[j].lower())) in (0, 1):
                anagrams[i] += 1
                anagrams[j] += 1
    return anagrams

def check_anagrams(lst):
    n = len(lst)
    sorted_anagrams = sorted(lst, key=lambda x: lst[x])
    pairs = 0
    last_pair = (0, 0)
    for anagrams, i in zip(sorted_anagrams, range(n)):
        if anagrams != last_pair[0] and anagrams > 1:
            pairs += 1
            last_pair = (anagrams, i)
        elif anagrams == last_pair[0] and i != last_pair[1]:
            last_pair = (anagrams, i)
    return pairs <= 59