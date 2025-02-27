from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_groups[sorted_string].append(string)
    anagram_pair_count = 0
    for group in anagram_groups.values():
        count = len(group)
        if count > 1:
            anagram_pair_count += count * (count - 1) // 2
    return anagram_pair_count >= 19