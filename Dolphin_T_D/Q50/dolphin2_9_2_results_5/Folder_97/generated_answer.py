def if_contains_anagrams(li):
    li = [s.lower() for s in li if len(s) >= 3]
    s = set()
    ct = 0
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if sorted(li[i]) == sorted(li[j]):
                s.add(li[i])
                ct += 1
    return ct >= 123