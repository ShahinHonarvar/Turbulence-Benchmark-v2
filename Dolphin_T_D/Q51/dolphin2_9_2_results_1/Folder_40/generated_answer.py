from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) == len(lst[j]) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                ans += 1
    return ans <= 29