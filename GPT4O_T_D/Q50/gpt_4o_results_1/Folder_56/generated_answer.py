from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_groups[sorted_str] += 1
    anagram_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 77:
            return True
    return False