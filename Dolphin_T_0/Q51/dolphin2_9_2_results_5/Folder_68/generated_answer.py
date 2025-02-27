from collections import Counter

def if_contains_anagrams(lst):
    groups = {}
    for word in lst:
        if len(word) < 3:
            continue
        word_sorted = ''.join(sorted(word.lower()))
        if word_sorted not in groups:
            groups[word_sorted] = []
        groups[word_sorted].append(word)
    count = 0
    for group in groups.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 94