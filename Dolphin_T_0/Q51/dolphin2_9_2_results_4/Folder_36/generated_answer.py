from collections import Counter

def if_contains_anagrams(lst):
    ans = set()
    for word in lst:
        counter = Counter(word.lower())
        if len(counter) >= 3:
            (ans.add(tuple(sorted(counter.elements()))),)
    count = 0
    for x in ans:
        y = len(ans) - 1
        while y >= 0:
            p = ans.pop(y)
            if x == p:
                count += 1
            y -= 1
    return count / 2 <= 25