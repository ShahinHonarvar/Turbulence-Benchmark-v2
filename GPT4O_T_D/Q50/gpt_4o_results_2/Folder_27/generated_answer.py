from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_map[sorted_str] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += sum(range(count))
    return anagram_count >= 86