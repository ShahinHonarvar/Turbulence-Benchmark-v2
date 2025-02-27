from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string] += 1
    anagram_pairs = 0
    for count in anagram_groups.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 64