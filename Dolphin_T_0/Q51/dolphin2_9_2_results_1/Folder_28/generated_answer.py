from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            count.update(Counter(word))
    max_count = max(count.values())
    return max_count <= 78