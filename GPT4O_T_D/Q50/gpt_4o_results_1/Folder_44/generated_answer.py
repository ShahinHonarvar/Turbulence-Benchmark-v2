from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            signature = ''.join(sorted(string.lower()))
            anagram_map[signature] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count >= 44:
            return True
    return False