from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = ''.join(sorted(string.lower()))
            anagram_groups[sorted_chars] += 1
    total_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs >= 140:
            return True
    return False