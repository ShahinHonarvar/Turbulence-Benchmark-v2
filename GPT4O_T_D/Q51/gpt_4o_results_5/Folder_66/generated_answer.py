from collections import Counter

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for string in strings:
        if len(string) >= 3:
            key = sorted_str(string)
            if key in anagram_groups:
                anagram_groups[key].append(string)
            else:
                anagram_groups[key] = [string]
    anagram_pairs_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            n = len(group)
            anagram_pairs_count += n * (n - 1) // 2
            if anagram_pairs_count > 64:
                return False
    return anagram_pairs_count <= 64