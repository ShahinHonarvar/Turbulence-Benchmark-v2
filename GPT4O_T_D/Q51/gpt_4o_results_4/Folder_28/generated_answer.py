from collections import defaultdict

def if_contains_anagrams(strings):

    def normalized_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = normalized_key(string)
            anagram_groups[key].append(string)
    pair_count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            pair_count += n * (n - 1) // 2
            if pair_count > 78:
                return False
    return pair_count <= 78