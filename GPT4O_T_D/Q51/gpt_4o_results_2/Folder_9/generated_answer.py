from collections import defaultdict

def if_contains_anagrams(words):
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_map = defaultdict(int)
    for word in normalized_words:
        anagram_map[word] += 1
    count_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return count_pairs <= 475