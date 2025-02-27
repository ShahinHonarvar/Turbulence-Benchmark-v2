from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for i in range(len(lst) - 1):
        if len(lst[i]) >= 3:
            key = ''.join(sorted(lst[i].lower()))
            if key not in counter.keys():
                counter[key] = 1
            else:
                counter[key] += 1
        if len(lst[i + 1:]) < 1:
            break
    return counter.most_common(1)[0][1] <= 41