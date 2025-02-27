from collections import defaultdict

def if_contains_anagrams(lst):
    grouped = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        grouped[key].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in grouped.values() if len(group[0]) >= 3))
    return anagram_pairs <= 57