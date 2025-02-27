from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_groups = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    for group_count in anagram_groups.values():
        if group_count > 1:
            count += group_count * (group_count - 1) // 2
    return count >= 155