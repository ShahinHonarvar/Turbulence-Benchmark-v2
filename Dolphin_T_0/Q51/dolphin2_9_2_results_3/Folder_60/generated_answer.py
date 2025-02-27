from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    anagram_counts = Counter()
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst_i = ''.join(sorted(lst[i].lower()))
                lst_j = ''.join(sorted(lst[j].lower()))
                if lst_i == lst_j:
                    anagram_counts[lst_i] += 1
                    count += 1
    for key in anagram_counts:
        pairs = anagram_counts[key] * (anagram_counts[key] - 1) // 2
        count += pairs
    return count <= 77