from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    anagram_groups = defaultdict(int)
    for word in normalized_words:
        anagram_groups[word] += 1
    for group_count in anagram_groups.values():
        if group_count > 1:
            count += group_count * (group_count - 1) // 2
    return count <= 57