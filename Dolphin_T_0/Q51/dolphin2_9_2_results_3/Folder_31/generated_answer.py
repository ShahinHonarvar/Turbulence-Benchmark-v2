from collections import Counter
    from itertools import groupby

def if_contains_anagrams(lst):
    count = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
    res = list(groupby(count.values(), key=lambda x: x // 2))
    if len([x for x, _ in res if x <= 65]) >= 65:
        return True
    else:
        return False