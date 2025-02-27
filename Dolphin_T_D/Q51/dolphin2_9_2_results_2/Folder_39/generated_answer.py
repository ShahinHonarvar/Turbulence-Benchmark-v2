from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    count = dict()
    for word in lst:
        w = ''.join(sorted(word)).lower()
        if len(w) >= 3:
            if w not in count:
                count[w] = 1
            else:
                count[w] += 1
    for val in count.values():
        if val > 1:
            ans += val * (val - 1) // 2
    if ans <= 257:
        return True
    else:
        return False