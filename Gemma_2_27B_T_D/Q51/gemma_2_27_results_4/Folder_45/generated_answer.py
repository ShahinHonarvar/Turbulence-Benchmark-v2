from collections import Counter

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        if len(word) >= 3:
            key = tuple(sorted(Counter(word.lower()).items()))
            anagram_groups.setdefault(key, []).append(word)
    count = 0
    for group in anagram_groups.values():
        count += len(group) * (len(group) - 1) // 2
    return count <= 464