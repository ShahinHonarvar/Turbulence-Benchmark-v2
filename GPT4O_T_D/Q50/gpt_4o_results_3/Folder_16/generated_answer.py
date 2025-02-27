from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized_map[normalize(s)].append(s)
    anagram_pairs = 0
    for words in normalized_map.values():
        if len(words) > 1:
            anagram_pairs += len(words) * (len(words) - 1) // 2
            if anagram_pairs >= 155:
                return True
    return False