from collections import defaultdict

def if_contains_anagrams(words):
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_groups = defaultdict(int)
    for word in normalized_words:
        anagram_groups[word] += 1
    pair_count = 0
    for count in anagram_groups.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
    return pair_count <= 29