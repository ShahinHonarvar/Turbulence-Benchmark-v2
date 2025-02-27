from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                if lst[i] not in anagrams:
                    anagrams[lst[i]] = []
                anagrams[lst[i]].append(lst[j])
    return Counter(anagrams.values())[1] <= 113