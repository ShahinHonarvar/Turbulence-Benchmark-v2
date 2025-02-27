from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            anagram_dict[normalized] += 1
    total_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs >= 93:
            return True
    return False