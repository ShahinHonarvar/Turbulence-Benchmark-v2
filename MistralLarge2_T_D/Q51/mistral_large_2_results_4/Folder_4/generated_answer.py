from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
    pairs_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return pairs_count <= 84