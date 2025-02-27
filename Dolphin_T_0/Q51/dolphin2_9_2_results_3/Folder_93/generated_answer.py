from collections import Counter

def if_contains_anagrams(lst):
    ans = set()
    for word in lst:
        if len(word) >= 3:
            ans.add(tuple(sorted(Counter(word.lower()))))
    return len(ans) <= 36