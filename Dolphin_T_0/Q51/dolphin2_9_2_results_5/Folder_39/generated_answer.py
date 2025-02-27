from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    sett = set()
    for word in lst:
        temp = ''.join(sorted(word.lower()))
        if len(temp) >= 3:
            cnt[temp] += 1
            sett.add(temp)
    ins = cnt.values()
    outs = [2 * i for i in ins]
    return list(map(lambda x: x in outs, ins))