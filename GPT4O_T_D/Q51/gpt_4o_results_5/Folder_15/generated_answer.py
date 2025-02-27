from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        normalized_word = ''.join(sorted(word.lower()))
        anagram_map[normalized_word].append(word)
    anagram_count = 0
    for group in anagram_map.values():
        filtered_group = [w for w in group if len(w) >= 3]
        if len(filtered_group) > 1:
            anagram_count += len(filtered_group) * (len(filtered_group) - 1) // 2
        if anagram_count > 20:
            return False
    return True