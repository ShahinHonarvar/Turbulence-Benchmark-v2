from collections import defaultdict

def if_contains_anagrams(lst):
    pairs_count = 0
    normalized_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            normalized_map[sorted_word] += 1
    for count in normalized_map.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count <= 43