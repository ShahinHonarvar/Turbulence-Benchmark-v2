from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[''.join(sorted(word.lower()))].append(word)
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 50