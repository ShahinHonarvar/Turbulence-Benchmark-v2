from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_groups[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return anagram_pairs <= 89