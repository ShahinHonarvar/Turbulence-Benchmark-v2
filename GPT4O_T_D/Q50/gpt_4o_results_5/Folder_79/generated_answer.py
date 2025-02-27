from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_map[normalize(string)].append(string)
    pairs_count = 0
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        if n > 1:
            pairs_count += n * (n - 1) // 2
            if pairs_count >= 40:
                return True
    return False