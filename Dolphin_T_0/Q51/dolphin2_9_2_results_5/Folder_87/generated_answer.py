from collections import Counter
    from itertools import permutations, combinations

def if_contains_anagrams(lst):
    ans = set()
    for word in lst:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            ans.add(word_sorted)
    cnt = 0
    for pair in combinations(ans, 2):
        if Counter(pair[0]) == Counter(pair[1]):
            cnt += 1
    return cnt <= 392