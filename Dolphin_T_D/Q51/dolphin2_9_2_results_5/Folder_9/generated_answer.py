from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    anagrams_found = 0
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    for count in c.values():
        if count > 1:
            anagrams_found += count * (count - 1) // 2
    return anagrams_found <= 475