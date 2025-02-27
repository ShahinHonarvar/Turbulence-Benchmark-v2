from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    anagram_pairs = {k: v // 2 for k, v in c.items() if v > 1}
    if sum(anagram_pairs.values()) <= 52:
        return True
    else:
        return False