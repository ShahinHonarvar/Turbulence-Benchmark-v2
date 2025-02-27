from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_groups[sorted_word].append(word)
    pair_count = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            pair_count += len(group) * (len(group) - 1) // 2
    return pair_count <= 20