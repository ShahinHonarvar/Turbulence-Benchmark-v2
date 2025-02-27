from collections import Counter

def if_contains_anagrams(list_strings):
    c = Counter()
    for word in list_strings:
        if len(word) < 3:
            continue
        word = word.lower()
        c[tuple(sorted(word))] += 1
    count_anagrams = sum((1 for v in c.values() if v > 1))
    return count_anagrams // 2 <= 86