from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    ans = []
    count_dict = {}
    ans_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        cown = Counter(word.lower())
        cown = ''.join([i + str(j) for i, j in cown.items()])
        if cown not in count_dict:
            count_dict[cown] = 1
        else:
            count_dict[cown] += 1
    for k, v in count_dict.items():
        if v > 81:
            ans.append(k)
    count_dict.clear()
    ans_dict.clear()
    return ans