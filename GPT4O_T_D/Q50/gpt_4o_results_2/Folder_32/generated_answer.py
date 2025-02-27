from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_groups[sorted_str] += 1
    anagram_pairs_count = 0
    for count in anagram_groups.values():
        if count > 1:
            anagram_pairs_count += count * (count - 1) // 2
        if anagram_pairs_count >= 194:
            return True
    return False