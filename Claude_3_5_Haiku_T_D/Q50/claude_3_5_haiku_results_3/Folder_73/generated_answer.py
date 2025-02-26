from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    signature_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = ''.join(sorted(string.lower()))
            signature_map[sorted_chars].append(string)
    for group in signature_map.values():
        if len(group) > 1:
            pair_count = len(group) * (len(group) - 1) // 2
            anagram_count += pair_count
    return anagram_count >= 91