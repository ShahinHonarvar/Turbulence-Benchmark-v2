from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_map[normalize(string)] += 1
    total_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2
            if total_pairs > 318:
                return False
    return True