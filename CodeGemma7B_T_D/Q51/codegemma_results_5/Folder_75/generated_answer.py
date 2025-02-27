from collections import defaultdict

def if_contains_anagrams(lst):
    counts = defaultdict(int)
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            counts[word] += 1
    return len(counts) <= 55