from collections import defaultdict

def if_contains_anagrams(strList):
    strLen = defaultdict(list)
    for s in strList:
        if len(s) >= 3:
            strLen[len(s)].append(s.lower())
    for k, v in strLen.items():
        v.sort()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if ''.join(sorted(v[i])) == ''.join(sorted(v[j])):
                    return True
    return False