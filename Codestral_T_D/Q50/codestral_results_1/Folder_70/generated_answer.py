from collections import defaultdict

def if_contains_anagrams(lst):
    groups = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            groups[sorted_word].append(word)
    anagram_pairs = 0
    for group in groups.values():
        anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 189