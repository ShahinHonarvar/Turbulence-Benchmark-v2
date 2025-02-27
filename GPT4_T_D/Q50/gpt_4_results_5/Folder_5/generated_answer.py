from collections import defaultdict

def if_contains_anagrams(lst):
    words = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            words[''.join(sorted(word.lower()))].append(word)
    count_pairs = sum((len(values) * (len(values) - 1) // 2 for values in words.values()))
    return count_pairs >= 21